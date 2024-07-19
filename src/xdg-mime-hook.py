import pcore
import os

def set_archiver(name):
    os.system(f"xdg-mime default {name}.desktop application/zip")
    os.system(f"xdg-mime default {name}.desktop application/x-tar")
    os.system(f"xdg-mime default {name}.desktop application/x-7z-compressed")
    os.system(f"xdg-mime default {name}.desktop application/x-rar-compressed")

if pcore.archiver == "file-roller":
    set_archiver("org.gnome.FileRoller")
else:
    set_archiver(f"{pcore.archiver}")

os.system(f"xdg-mime default {pcore.file_manager}.desktop inode/directory")