import argparse

from koradctl.types import human_bool

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
        help='the serial port baudrate',
    )
    parser.add_argument('-I', '--interactive',
        dest='interactive',
        action='store_true',
        default=False,
        help='enable interactive mode',
    )
    parser.add_argument('-t', '--test',
        dest='test',
        action='store_true',
        default=False,
        help='run the tests and quit',
    )
    parser.add_argument('-v', '--voltage',
        type=float,
        dest='voltage',
        action='store',
        default=None,
        help='set the voltage',
    )
    parser.add_argument('-i', '--current',
        type=float,
        dest='current',
        action='store',
        default=None,
        help='set the current',
    )
    parser.add_argument('-e', '--enable',
        type=human_bool,
        dest='output_enable',
        action='store',
        default=None,
        help='set the output enable',
    )
    return parser

def get_args():
    parser = get_arg_parser()
    return parser.parse_args()
