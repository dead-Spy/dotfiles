if status is-interactive
# Commands to run in interactive sessions can go here
end

starship init fish | source

function up
    cd ~/dotfiles
    git add .
    
    if count $argv > /dev/null
        git commit -m "$argv"
    else
        git commit -m "sync: updated on (date '+%Y-%m-%d %H:%M:%S')"
    end
    
    git push
    cd -
end
if test -f ~/.config/fish/weather_key.fish
    source ~/.config/fish/weather_key.fish
end
