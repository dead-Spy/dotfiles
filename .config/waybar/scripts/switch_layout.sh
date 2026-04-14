#!/bin/bash

CONFIG_DIR="$HOME/.config/waybar"
CONFIGS="$CONFIG_DIR/configs"
THEMES="$CONFIG_DIR/themes"

SINGLE_CONF="$CONFIGS/single.jsonc"
SEP_CONF="$CONFIGS/separated.jsonc"
SINGLE_CSS="$THEMES/single.css"
SEP_CSS="$THEMES/separated.css"

if [ ! -L "$CONFIG_DIR/config.jsonc" ] || ls -l "$CONFIG_DIR/config.jsonc" | grep -q "single.jsonc"; then
    ln -sf "$SEP_CONF" "$CONFIG_DIR/config.jsonc"
    ln -sf "$SEP_CSS" "$CONFIG_DIR/style.css"
    notify-send "Waybar Layout" "Switched to Separated Layout" -i display
else
    ln -sf "$SINGLE_CONF" "$CONFIG_DIR/config.jsonc"
    ln -sf "$SINGLE_CSS" "$CONFIG_DIR/style.css"
    notify-send "Waybar Layout" "Switched to Single Layout" -i display
fi

pkill waybar
waybar &