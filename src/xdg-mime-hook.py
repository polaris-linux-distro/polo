import pcore
import os
import configparser

def config_usr():
    configparser_ = configparser.ConfigParser()
    configparser_.read(f"{os.path.expanduser("~")}/usr.conf")
    return configparser_

cfgusr = config_usr()
editor = cfgusr["conf"]["editor"]
terminal = cfgusr["conf"]["terminal"]
browser = cfgusr["conf"]["browser"]
file_manager = cfgusr["conf"]["filemanager"]
archiver = cfgusr["conf"]["archiver"]
pdf_viewer = cfgusr["conf"]["pdfviewer"]
image_viewer = cfgusr["conf"]["imageviewer"]
media_player = cfgusr["conf"]["mediaplayer"]

# Archiver
os.system(f"xdg-mime default {archiver}.desktop application/zip")
os.system(f"xdg-mime default {archiver}.desktop application/x-tar")
os.system(f"xdg-mime default {archiver}.desktop application/x-7z-compressed")
os.system(f"xdg-mime default {archiver}.desktop application/x-rar-compressed")

# File Manager
os.system(f"xdg-mime default {file_manager}.desktop inode/directory")

# Browser
os.system(f"xdg-mime default {browser}.desktop text/html")
os.system(f"xdg-mime default {browser}.desktop application/xhtml+xml")
os.system(f"xdg-mime default {browser}.desktop application/xml")
os.system(f"xdg-mime default {browser}.desktop text/xml")

# PDF viewer (pretty much just the web browser, but if they want libreoffice this is good)
os.system(f"xdg-mime default {pdf_viewer}.desktop application/pdf")

# Image viewer
os.system(f"xdg-mime default {image_viewer}.desktop image/jpeg")
os.system(f"xdg-mime default {image_viewer}.desktop image/png")
os.system(f"xdg-mime default {image_viewer}.desktop image/gif")
os.system(f"xdg-mime default {image_viewer}.desktop image/bmp")
os.system(f"xdg-mime default {image_viewer}.desktop image/tiff")
os.system(f"xdg-mime default {image_viewer}.desktop image/webp")
os.system(f"xdg-mime default {image_viewer}.desktop image/svg+xml")
os.system(f"xdg-mime default {image_viewer}.desktop image/heif")
os.system(f"xdg-mime default {image_viewer}.desktop image/heic")

# Media player
os.system(f"xdg-mime default {media_player}.desktop video/mp4")
os.system(f"xdg-mime default {media_player}.desktop video/webm")
os.system(f"xdg-mime default {media_player}.desktop video/x-matroska")
os.system(f"xdg-mime default {media_player}.desktop video/avi")
os.system(f"xdg-mime default {media_player}.desktop video/mpeg")
os.system(f"xdg-mime default {media_player}.desktop video/quicktime")
os.system(f"xdg-mime default {media_player}.desktop video/x-msvideo")
os.system(f"xdg-mime default {media_player}.desktop video/x-flv")
os.system(f"xdg-mime default {media_player}.desktop video/x-ms-wmv")
os.system(f"xdg-mime default {media_player}.desktop video/ogg")

# Media player (audio)
os.system(f"xdg-mime default {media_player}.desktop audio/mpeg")
os.system(f"xdg-mime default {media_player}.desktop audio/ogg")
os.system(f"xdg-mime default {media_player}.desktop audio/wav")
os.system(f"xdg-mime default {media_player}.desktop audio/flac")
os.system(f"xdg-mime default {media_player}.desktop audio/aac")
os.system(f"xdg-mime default {media_player}.desktop audio/x-ms-wma")
os.system(f"xdg-mime default {media_player}.desktop audio/x-matroska")
os.system(f"xdg-mime default {media_player}.desktop audio/x-wav")
os.system(f"xdg-mime default {media_player}.desktop audio/webm")
os.system(f"xdg-mime default {media_player}.desktop video/midi")