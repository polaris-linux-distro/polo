import configparser

VERSION = 1.0

# its config time (and then i configurated all over the place)

def config():
    configparser_ = configparser.ConfigParser()
    configparser_.read("/etc/polaris/sys.conf")
    return configparser_

def config_usr():
    configparser_ = configparser.ConfigParser()
    configparser_.read("/etc/polaris/usr.conf")
    return configparser_

cfg = config()
cfgusr = config_usr()
ostype = cfg["conf"]["type"]
ostask = cfg["conf"]["task"]
terminal = cfgusr["conf"]["terminal"]