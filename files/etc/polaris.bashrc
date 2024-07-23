#
# /etc/bash.bashrc
#

# If not running interactively, don't do anything

alias cd..="cd .."
alias cd.="cd ."

GREEN="\[\e[1;32m\]"
BLUE="\[\e[1;34m\]" 
RESET="\[\e[0m\]"

export XDG_DATA_DIRS="/var/lib/flatpak/exports/share:$HOME/.local/share/flatpak/exports/share:$XDG_DATA_DIRS"
export EDITOR=$(get_ini_value "conf" "editor" "$HOME/usr.conf")
export TERMINAL=$(get_ini_value "conf" "terminal" "$HOME/usr.conf")
export BROWSER=$(get_ini_value "conf" "browser" "$HOME/usr.conf")
