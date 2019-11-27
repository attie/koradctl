import sys
from serial.serialutil import SerialException

from koradctl.cli import Cli

if __name__ == '__main__':
    try:
        cli = Cli()
        cli.run()
    except KeyboardInterrupt:
        pass
    except SerialException:
        print('ERROR: The power supply appears to have gone away...', file=sys.stderr)
