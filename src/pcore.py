import configparser
import os

VERSION = 1.0

# its config time (and then i configurated all over the place)

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