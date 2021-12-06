module.exports = class boardSelection {
    constructor(boardType, port) {
        this.type = boardType;

    }

    getBoard() {
        var prop = null;

        if (port != null) {
            prop = {
                io: null,
                port: port
            }
        }else{
            prop = {
                io: null
            }
        }

        var board = null;
        switch (this.type) {
            case 'rasp':
                prop.io = new Raspi();
                break;
            case 'beagle':
                prop.io = new BeagleBone();
                break;
            case 'galileo':
                prop.io = new Joule();
                break;
            case 'bean':
                var boardIO = new beanio.Board();
                prop.io = 

        }

        board = new five.Board(prop);
        return board;
    }
}