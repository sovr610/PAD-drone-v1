var myArgs = process.argv.slice(2);
console.log('myArgs: ', myArgs);
const five = require('johnny-five');
var beagle = require('beaglebone-io');
var blend = require('blend-micro-io');
var galileo = require('galileo-io');
var bean = require('bean-io');
var nino = require('nino-io');
var pcduino = require('pcduino-io');
Pinoccio-IO
Raspi-IO
Spark-IO
Imp-IO
Remote-IO
Board-IO
Tessel-IO
Playground-IO

var net = require('net');




if(myArgs.length == 0){
    console.log('please enter the arguments. arg1 -> board type, arg2 -> port');
}

var boardSelect = require('./boardSelect');
var board = new boardSelect(myArgs[0], myArgs[1]);

board.on('ready', () => {
    const server = net.createServer((socket)=>{
        console.log('client connected');

        socket.on('data',(data)=>{

        });

        socket.on('end', ()=>{
            console.log('server disconnect');
        })
    })

    server.on('error', (err)=>{
        console.error(err);
    })

    server.listen(6677,() => {
        console.log('boud server to port 6677');
    })
  // Create an Led on pin 7 (GPIO4) on P1 and strobe it on/off
  // Optionally set the speed; defaults to 100ms
  (new five.Led('P1-7')).strobe();

});

