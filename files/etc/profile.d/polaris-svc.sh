#!/bin/bash

# this stuffs a bit hacky

source /etc/polaris/lib.sh

export EDITOR=$(/usr/bin/python3 /usr/share/polaris/pcore-shack.py editor)
export XDG_DATA_DIRS="/var/lib/flatpak/exports/share:$HOME/.local/share/flatpak/exports/share:$XDG_DATA_DIRS"
export TERMINAL=$(/usr/bin/python3 /usr/share/polaris/pcore-shack.py terminal)
export BROWSER=$(/usr/bin/python3 /usr/share/polaris/pcore-shack.py browser)

PATH="$PATH:/usr/share/polaris"

nohup qlipper &
/usr/bin/python /usr/share/polaris/polokeys_user.py