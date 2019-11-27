from koradctl.args import get_args
from koradctl.port import get_port
from koradctl.psu import PowerSupply

from koradctl.test import TestSuite

from time import sleep

class Cli:
    def __init__(self):
        self.args = get_args()
        self.port = get_port(self.args.port, self.args.baudrate)
        self.psu = PowerSupply(self.port)

    def run(self):
        if self.args.test:
            t = TestSuite(self.psu)
            t.run()
            exit(0)

        if self.args.interactive:
            raise NotImplementedError()

        # todo
