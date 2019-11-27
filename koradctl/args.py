import argparse

def get_arg_parser():
    parser = argparse.ArgumentParser(
        description='Korad Power Supply Controller',
    )
    parser.add_argument('-p', '--port',
        type=str,
        dest='port',
        action='store',
        default='/dev/ttyACM0',
        help='the serial port to use',
    )
    parser.add_argument('-b', '--baud',
        type=int,
        dest='baudrate',
        action='store',
        default=9600,
    )
    parser.add_argument('-i', '--interactive',
        dest='interactive',
        action='store_true',
        default=False,
    )
    parser.add_argument('-t', '--test',
        dest='test',
        action='store_true',
        default=False,
    )
    return parser

def get_args():
    parser = get_arg_parser()
    return parser.parse_args()
