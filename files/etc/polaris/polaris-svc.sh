#!/bin/bash

# this stuffs a bit hacky

/usr/bin/python /usr/share/polaris/polokeys_user.py
/usr/bin/python /usr/share/polaris/default-hack.py

export XDG_DATA_DIRS="/var/lib/flatpak/exports/share:$HOME/.local/share/flatpak/exports/share:$XDG_DATA_DIRS"