import distro
import subprocess
import os
import sys
import platform

print('running')

board = sys.argv[0]

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
        if board == 'beaglebone':
            subprocess.check_call("./scripts/debian/arm/beagleBone/install_npm.sh", shell=True)
        if board == 'blend-micro':
            subprocess.check_call("./scripts/debian/arm/blend-micro/install_npm.sh", shell=True)
        if board == 'galileo-io':
            subprocess.check_call("./scripts/debian/arm/Galileo/install_npm.sh", shell=True)
        if board == 'bean-io':
            subprocess.check_call("./scripts/debian/arm/bean/install_npm.sh", shell=True)
        if board == 'nino-io':
            subprocess.check_call("./scripts/debian/arm/nino/install_npm.sh", shell=True)
        if board == 'pcduino-io':
            subprocess.check_call("./scripts/debian/arm/pcDuino/install_npm.sh", shell=True) 
        if board == 'pinoccio-io':
            subprocess.check_call("./scripts/debian/arm/Piniccio-Scout/install_npm.sh", shell=True)    
        if board == 'raspberry-pi':
            subprocess.check_call("./scripts/debian/arm/raspberry_pi/install_npm.sh", shell=True)
        if board == 'spark-io':
            subprocess.check_call("./scripts/debian/arm/spark/install_npm.sh", shell=True)
        if board == 'imp-io':
            subprocess.check_call("./scripts/debian/arm/imp/install_npm.sh", shell=True)
        if board == 'remote-io':
            subprocess.check_call("./scripts/debian/arm/remote/install_npm.sh", shell=True)
        if board == 'general':
            subprocess.check_call("./scripts/debian/arm/generic/install_npm.sh", shell=True)
        if board == 'tessel':
            subprocess.check_call("./scripts/debian/arm/tessel/install_npm.sh", shell=True)
        if board == 'playground':
            subprocess.check_call("./scripts/debian/arm/playground/install_npm.sh", shell=True)
        if board == 'x86':
            subprocess.check_call("./scripts/debian/arm/install_npm.sh", shell=True)


if platform.system()  == 'Windows':
    subprocess.check_call("./scripts/windows/nodeInstall.ps1", shell=True)
    if board == 'beaglebone':
        subprocess.check_call("./scripts/debian/arm/beagleBone/install_npm.sh", shell=True)
    if board == 'blend-micro':
        subprocess.check_call("./scripts/debian/arm/blend-micro/install_npm.sh", shell=True)
    if board == 'galileo-io':
        subprocess.check_call("./scripts/debian/arm/Galileo/install_npm.sh", shell=True)
    if board == 'bean-io':
        subprocess.check_call("./scripts/debian/arm/bean/install_npm.sh", shell=True)
    if board == 'nino-io':
        subprocess.check_call("./scripts/debian/arm/nino/install_npm.sh", shell=True)
    if board == 'pcduino-io':
        subprocess.check_call("./scripts/debian/arm/pcDuino/install_npm.sh", shell=True) 
    if board == 'pinoccio-io':
        subprocess.check_call("./scripts/windows/arm/Piniccio-Scout/install_npm.bat", shell=True)    
    if board == 'raspberry-pi':
        subprocess.check_call("./scripts/windows/arm/raspberry_pi/install_npm.bat", shell=True)
    if board == 'spark-io':
        subprocess.check_call("./scripts/windows/arm/spark/install_npm.bat", shell=True)
    if board == 'imp-io':
        subprocess.check_call("./scripts/windows/arm/imp/install_npm.bat", shell=True)
    if board == 'remote-io':
        subprocess.check_call("./scripts/windows/arm/remote/install_npm.bat", shell=True)
    if board == 'general':
        subprocess.check_call("./scripts/windows/arm/generic/install_npm.bat", shell=True)
    if board == 'tessel':
        subprocess.check_call("./scripts/windows/arm/tessel/install_npm.bat", shell=True)
    if board == 'playground':
        subprocess.check_call("./scripts/windows/arm/playground/install_npm.bat", shell=True)
    if board == 'x86':
        subprocess.check_call("./scripts/windows/arm/install_npm.bat", shell=True)



