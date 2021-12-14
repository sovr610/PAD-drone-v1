const shell = require('shelljs')

module.exports = class odyssey{
    constructor() {
        this.platform = process.platform;
        this.pins = [
            {

            }
        ]
    }

    sePin(pin, inOut, value) {
        if(this.platform === 'linux') {
            shell.exec('sudo i');
            shell.exec('cd /sys/class/gpio');
            shell.exec('echo ' + pin + ' > export');
            shell.exec('cd gpio' + pin);
            
        }

    }

    sudo -i
cd /sys/class/gpio
echo 337 > export
cd gpio337
echo "out" > direction
echo 1 > value
}