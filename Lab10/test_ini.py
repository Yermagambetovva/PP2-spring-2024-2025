from configparser import ConfigParser

parser = ConfigParser()
parser.read('database.ini')

print(parser.sections())
