import distro
import subprocess
import os
import sys
import platform

print('running')

def is_raspberrypi():
    try:
        with io.open('/sys/firmware/devicetree/base/model', 'r') as m:
            if 'raspberry pi' in m.read().lower(): return True
    except Exception: pass
    return False

def machine():
    """Return type of machine."""
    if os.name == 'nt' and sys.version_info[:2] < (2,7):
        return os.environ.get("PROCESSOR_ARCHITEW6432", 
               os.environ.get('PROCESSOR_ARCHITECTURE', ''))
    else:
        return platform.machine()

def os_bits(machine=machine()):
    """Return bitness of operating system, or None if unknown."""
    machine2bits = {'AMD64': 64, 'x86_64': 64, 'i386': 32, 'x86': 32}
    return machine2bits.get(machine, None)

dist = distro.id()
print(machine())
print(platform.system())

if platform.system() == 'Linux':
    if dist == 'ubuntu' or is_raspberrypi():
        subprocess.check_call("./scripts/debian/installNode.sh", shell=True)
        subprocess.check_call("./scripts/arm/install_npm.sh", shell=True)
if platform.system()  == 'Windows':
    print('none')



