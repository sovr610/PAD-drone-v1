import ConfigParser
from subprocess import call
from os.path import exists

parser = ConfigParser.ConfigParser()
parser.read('board.config')

board = parser.get('main','board')

file_exists = exists('installed.dat')

if file_exists == False:
    rc = call("python3 /setup/install.py " + board, shell=True)
else:
    rc = call("node /src/core.js " + board, shell=True)
