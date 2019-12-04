import serial

def get_port(port: str, baudrate: int = 9600) -> serial.Serial:
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
