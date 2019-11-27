import argparse

from koradctl.types import human_bool

def get_arg_parser():
    parser = argparse.ArgumentParser(prog='koradctl', description='Korad Power Supply Controller')

    parser.add_argument('-p', '--port',         type=str,        dest='port',                    action='store',      default='/dev/ttyACM0', help='the serial port to use')
    parser.add_argument('-b', '--baud',         type=int,        dest='baudrate',                action='store',      default=9600,           help='the serial port baudrate')

    parser.add_argument('-I', '--interactive',                   dest='interactive',             action='store_true', default=False,          help='enable interactive mode')
    parser.add_argument('-t', '--test',                          dest='test',                    action='store_true', default=False,          help='run the tests and quit')

    parser.add_argument(      '--ocp',          type=human_bool, dest='over_current_protection', action='store', default=None,      help='set the over current protection')
    parser.add_argument(      '--ovp',          type=human_bool, dest='over_voltage_protection', action='store', default=None,      help='set the over current protection')

    parser.add_argument('-v', '--voltage',      type=float,      dest='voltage',                 action='store',      default=None,           help='set the voltage')
    parser.add_argument('-i', '--current',      type=float,      dest='current',                 action='store',      default=None,           help='set the current')
    parser.add_argument('-e', '--enable',       type=human_bool, dest='output_enable',           action='store',      default=None,           help='set the output enable')

    parser.add_argument('-m', '--monitor',                       dest='monitor',                 action='store_true', default=False,          help='monitor the supply (one reading)')
    parser.add_argument('-M', '--monitor-loop',                  dest='monitor_loop',            action='store_true', default=False,          help='monitor the supply (forever)')
    parser.add_argument('-f', '--monitor-freq', type=float,      dest='monitor_freq',            action='store',      default=1,              help='frequency of monitor readings, in seconds')

    return parser

def get_args():
    parser = get_arg_parser()
    return parser.parse_args()
