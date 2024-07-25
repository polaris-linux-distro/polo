#!/bin/bash
export XDG_DATA_DIRS="/var/lib/flatpak/exports/share:$HOME/.local/share/flatpak/exports/share:$XDG_DATA_DIRS"

PATH="$PATH:/usr/share/polaris"

nohup qlipper &
/usr/bin/python /usr/share/polaris/polokeys_user.py