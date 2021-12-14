import ConfigParser
from subprocess import call
from os.path import exists

parser = ConfigParser.ConfigParser()
parser.read('main.config')

board = parser.get('main','board')

file_exists = exists('installed.dat')

if file_exists == False:
    rc = call("python3 /setup/install.py " + board, shell=True)
    f = open("installed.dat", "a")
    f.write("installed, hows your day been?")
    f.close()
else:
    rc = call("node /src/core.js " + board, shell=True)
