#!/bin/bash

# this stuffs a bit hacky

source /etc/polaris/lib.sh

export XDG_DATA_DIRS="/var/lib/flatpak/exports/share:$HOME/.local/share/flatpak/exports/share:$XDG_DATA_DIRS"

export TERMINAL=$(get_ini_value "conf" "terminal" "$HOME/usr.conf")
export BROWSER=$(get_ini_value "conf" "browser" "$HOME/usr.conf")
export EDITOR=$(get_ini_value "conf" "editor" "$HOME/usr.conf")

/usr/bin/python /usr/share/polaris/polokeys_user.py