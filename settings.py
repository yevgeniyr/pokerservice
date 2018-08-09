import configparser
import pprint

def init():
    global config
    config = configparser.ConfigParser(delimiters=('='))
    config.read( [ 'poker.conf' ] )
    pprint.pprint(config.items('network'))
