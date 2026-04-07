#!/usr/bin/env python3
import json
import sys
import gi
gi.require_version('Playerctl', '2.0')
from gi.repository import Playerctl, GLib

def get_icon(name):
    if "spotify" in name.lower():
        return ""
    return "󰎆"

def on_metadata(player, metadata, manager):
    render(manager)

def on_play_pause(player, status, manager):
    render(manager)

def on_name_appeared(manager, name):
    init_player(name, manager)

def init_player(name, manager):
    player = Playerctl.Player.new_from_name(name)
    player.connect('metadata', on_metadata, manager)
    player.connect('playback-status', on_play_pause, manager)
    render(manager)

def render(manager):
    players = manager.props.players
    if not players:
        print(json.dumps({"text": "", "class": "custom-media", "alt": "default"}))
        sys.stdout.flush()
        return

    player = players[0]
    title = player.get_title()
    artist = player.get_artist()
    status = player.get_property("playback-status")

    if not title:
        title = "Unknown Title"
    
    output = f"{artist} - {title}" if artist else title
    icon = get_icon(player.props.player_name)
    
    data = {
        "text": output,
        "class": "custom-media",
        "alt": player.props.player_name,
        "icon": icon
    }
    
    print(json.dumps(data))
    sys.stdout.flush()

manager = Playerctl.PlayerManager()
manager.connect('name-appeared', on_name_appeared)

for name in manager.props.player_names:
    init_player(name, manager)

GLib.MainLoop().run()
