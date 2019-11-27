import sys
from serial.serialutil import SerialException

from koradctl.cli import Cli

def cli():
    try:
        cli_app = Cli()
        cli_app.run()
    except KeyboardInterrupt:
        pass
    except SerialException:
        print('ERROR: The power supply appears to have gone away...', file=sys.stderr)

if __name__ == '__main__':
    cli()
