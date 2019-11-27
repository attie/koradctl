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

        if self.args.voltage is not None:
            self.psu.set_voltage_setpoint(self.args.voltage)
            print('Voltage: request: %2.2f, result: %2.2f' % (
                self.args.voltage,
                self.psu.get_voltage_setpoint().value,
            ))

        if self.args.current is not None:
            self.psu.set_current_setpoint(self.args.current)
            print('Current: request: %1.3f, result: %1.3f' % (
                self.args.current,
                self.psu.get_current_setpoint().value,
            ))

        if self.args.output_enable is not None:
            self.psu.set_output_state(self.args.output_enable)
            print('Enable:  request: %-5s, result: %-5s' % (
                'On' if self.args.output_enable else 'Off',
                'On' if self.psu.get_output_state() else 'Off',
            ))
