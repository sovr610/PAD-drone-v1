var myArgs = process.argv.slice(2);
var board = null;
console.log('myArgs: ', myArgs);


const five = require('johnny-five');

switch(myArgs[0]){
    case 'beaglebone':
        board = require('beaglebone-io');
        break;
    case 'blend-micro':
        board = require('blend-micro-io');
        break;
    case 'galileo-io':
        board = require('galileo-io');
        break;
    case 'bean-io':
        board = require('bean-io');
        break;
    case 'nino-io':
        board = require('nino-io');
        break;
    case 'pcduino-io':
        board = require('pcduino-io');
        break;
    case 'pinoccio-io':
        board = require('pinoccio-io');
        break;
    case 'raspberry-pi':
        board = require('raspi-io');
        break;
    case 'spark-io':
        board = require('spark-io');
        break;
    case 'imp-io':
        board = require('imp-io');
        break;
    case 'remote-io':
        board = require('remote-io');
        break;
    case 'general':
        board = require('board-io');
        break;
    case 'tessel':
        board = require('tessel-io');
        break;
    case 'playground':
        board = require('playground-io');
        break;
}

//var beagle = require('beaglebone-io');
//var blend = require('blend-micro-io');
//var galileo = require('galileo-io');
//var bean = require('bean-io');
//var nino = require('nino-io');
//var pcduino = require('pcduino-io');
//var pinoccio = require('Pinoccio-IO');
//var rasp = require('Raspi-IO');
//var spark = require('Spark-IO');
//var imp = require('Imp-IO');
//var remote_io = require('Remote-IO');
//var genBoard = require('Board-IO');
//var tessel = require('Tessel-IO');
//var playgroundBoard = require('Playground-IO');

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

