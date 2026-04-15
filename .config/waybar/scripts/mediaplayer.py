#!/usr/bin/env python3
import json
import sys
import gi
import html
gi.require_version('Playerctl', '2.0')
from gi.repository import Playerctl, GLib

def get_icon(name):
    name = name.lower()
    if "spotify" in name: return ""
    if "vlc" in name: return "󰕼"
    if "chromium" in name or "chrome" in name: return ""
    if "firefox" in name: return ""
    return "󰎆"

def render(manager):
    players = manager.props.players
    
    if not players:
        print(json.dumps({"text": "Nothing Playing", "class": "stopped", "alt": "default", "icon": "󰎆"}))
        sys.stdout.flush()
        return

    player = players[0]
    for p in players:
        if p.get_property("playback-status") == Playerctl.PlaybackStatus.PLAYING:
            player = p
            break

    title = player.get_title()
    artist = player.get_artist()
    status = player.get_property("playback-status")

    if not title and not artist:
        print(json.dumps({"text": "Nothing Playing", "class": "stopped", "alt": "default", "icon": "󰎆"}))
        sys.stdout.flush()
        return
    
    status_str = "stopped"
    if status == Playerctl.PlaybackStatus.PLAYING: status_str = "playing"
    elif status == Playerctl.PlaybackStatus.PAUSED: status_str = "paused"

    if artist and title:
        clean_artist = artist.lower().replace("vevo", "").strip()
        if clean_artist in title.lower():
            output = title
        else:
            output = f"{artist} - {title}"
    else:
        output = title or artist or "Unknown"

    output = html.escape(output)
    
    data = {
        "text": output,
        "class": status_str,
        "alt": player.props.player_name,
        "icon": get_icon(player.props.player_name)
    }
    
    print(json.dumps(data))
    sys.stdout.flush()

manager = Playerctl.PlayerManager()

def on_name_appeared(manager, name):
    init_player(name)

def init_player(name):
    try:
        player = Playerctl.Player.new_from_name(name)
        player.connect('metadata', lambda p, m: render(manager))
        player.connect('playback-status', lambda p, s: render(manager))
        manager.manage_player(player)
        render(manager)
    except Exception:
        pass

manager.connect('name-appeared', on_name_appeared)
manager.connect('player-vanished', lambda m, p: render(m))

for name in manager.props.player_names:
    init_player(name)

if not manager.props.player_names:
    render(manager)

GLib.MainLoop().run()