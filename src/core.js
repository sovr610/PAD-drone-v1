var myArgs = process.argv.slice(2);
console.log('myArgs: ', myArgs);
const five = require('johnny-five');


if(myArgs.length == 0){
    console.log('please enter the arguments. arg1 -> board type, arg2 -> port');
}

var boardSelect = require('./boardSelect');
var board = new boardSelect(myArgs[0], myArgs[1]);



board.on('ready', () => {

  // Create an Led on pin 7 (GPIO4) on P1 and strobe it on/off
  // Optionally set the speed; defaults to 100ms
  (new five.Led('P1-7')).strobe();

});