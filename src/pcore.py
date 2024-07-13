import configparser

VERSION = 1.0

# its config time (and then i configurated all over the place)

def config():
    configparser_ = configparser.ConfigParser()
    configparser_.read("/etc/polaris/sys.conf")
    return configparser_

cfg = config()
ostype = cfg["conf"]["type"]
ostask = cfg["conf"]["task"]
terminal = cfg["conf"]["terminal"]