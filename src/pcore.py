import configparser
import os

VERSION = 1.0

# its config time (and then i configurated all over the place)

def config():
    configparser_ = configparser.ConfigParser()
    configparser_.read("/etc/polaris/sys.conf")
    return configparser_

def config_usr():
    configparser_ = configparser.ConfigParser()
    configparser_.read(f"{os.path.expanduser("~")}/usr.conf")
    return configparser_

cfg = config()
cfgusr = config_usr()
ostype = cfg["conf"]["type"]
ostask = cfg["conf"]["task"]
terminal = cfgusr["conf"]["terminal"]
browser = cfgusr["conf"]["browser"]
editor = cfgusr["conf"]["editor"]