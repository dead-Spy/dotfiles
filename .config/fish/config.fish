if status is-interactive
    # Commands to run in interactive sessions can go here
end

starship init fish | source

if test -f ~/.config/fish/weather_key.fish
    source ~/.config/fish/weather_key.fish
end

set -g fish_greeting ""
fastfetch

function setwall
    swww img $argv[1] --transition-type grow --transition-pos 0.85,0.97 --transition-step 90
    wal -i $argv[1]
end