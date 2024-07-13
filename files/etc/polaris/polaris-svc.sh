#!/bin/bash

# this stuffs a bit hacky

export XDG_DATA_DIRS="/var/lib/flatpak/exports/share:$HOME/.local/share/flatpak/exports/share:$XDG_DATA_DIRS"

/usr/bin/python /usr/share/polaris/default-hack.py

/usr/bin/python /usr/share/polaris/polokeys_user.py