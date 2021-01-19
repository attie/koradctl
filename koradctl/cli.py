import sys
from time import sleep
from serial.serialutil import SerialException

from koradctl.args import get_args
from koradctl.port import get_port
from koradctl.psu import PowerSupply
from koradctl.test import TestSuite

class Cli:
    def __init__(self):
        self.args = get_args()

        if self.args.show_version:
            import koradctl.package as me
            print('%s version %s' % ( me.proj_name, me.version ))
            exit(0)

        try:
            self.port = get_port(self.args.port, self.args.baudrate)
        except SerialException:
            print('ERROR: Failed to connect to the power supply...', file=sys.stderr)
            exit(0)

        self.psu = PowerSupply(self.port)

    def run(self):
        if self.args.test:
            self.run_tests()
        elif self.args.interactive:
            self.run_interactive()
        else:
            self.run_noninteractive()

    def run_tests(self):
        t = TestSuite(self.psu)
        t.run()

    def run_interactive(self):
        raise NotImplementedError()

    def run_noninteractive(self):
        if not self.psu.is_tested():
            print('WARNING: this power supply is not fully tested', file=sys.stderr)

        if self.args.over_current_protection is not None:
            self.psu.set_ocp_state(self.args.over_current_protection)
            print('OCP:     request: %-5s' % (
                'On' if self.args.over_current_protection else 'Off',
            ))

        if self.args.over_voltage_protection is not None:
            self.psu.set_ovp_state(self.args.over_voltage_protection)
            print('OVP:     request: %-5s' % (
                'On' if self.args.over_voltage_protection else 'Off',
            ))

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
            if self.args.output_enable == 'toggle':
                new_state = not self.psu.get_output_state()
            else:
                new_state = self.args.output_enable

            self.psu.set_output_state(new_state)
            print('Enable:  request: %-5s, result: %-5s' % (
                'On' if new_state else 'Off',
                'On' if self.psu.get_output_state() else 'Off',
            ))

        if self.args.monitor or self.args.monitor_loop:
            self.print_output_readings()

        if self.args.monitor_loop:
            try:
                while True:
                    sleep(self.args.monitor_freq)
                    self.print_output_readings()
            except KeyboardInterrupt:
                print('') # this puts the terminal's ^C on a line by itself

        if self.args.off_on_exit:
            self.psu.set_output_state(False)
            print('Enable:  request: %-5s, result: %-5s' % (
                'Off',
                'On' if self.psu.get_output_state() else 'Off',
            ))

    def print_output_readings(self):
        v, i, p = self.psu.get_output_readings()
        print('Output: %1.3f A, %2.2f v, %2.2f W' % (
            i.value, v.value, p.value
        ))
