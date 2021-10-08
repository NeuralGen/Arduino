def Find_Arduino():
    import serial.tools.list_ports
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "Arduino" in p.description:
            Port = (p[0])

    return Port


class Arduino:
    def __init__(self, port):
        import pyfirmata
        self.board = pyfirmata.Arduino(port)

    def Write(self, pin, state):
        self.board.digital[pin].write(state)

    def Read(self, pin):
        return self.board.analog[pin].read()


if __name__ == "__main__":
    import time
    
    arduino = Arduino(Find_Arduino())
    while True:
        arduino.Write(13, 0)
        time.sleep(1)
        arduino.Write(13, 1)
        time.sleep(1)

    
