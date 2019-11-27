import serial

def get_port(port, baudrate=9600):
    return serial.Serial(
        port=port,
        baudrate=baudrate,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=0.100, # 100ms
        xonxoff=False,
        rtscts=False,
        exclusive=True,
    )
