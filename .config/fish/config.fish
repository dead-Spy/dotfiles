if status is-interactive
    # Commands to run in interactive sessions can go here
end

starship init fish | source

if test -f ~/.config/fish/weather_key.fish
    source ~/.config/fish/weather_key.fish
end

set -g fish_greeting ""
fastfetch