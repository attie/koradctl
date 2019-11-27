from koradctl.pretty import pretty_status, pretty_reading

# i used the sigrok page for reference:
#     https://sigrok.org/wiki/Korad_KAxxxxP_series
#
# i have a Tenma 72-2540, and the only discrepancy i've found is
# in the status byte, where bit 7 (0x80) indicates the "OVP and/or
# OCP status", instead of bit 5 (0x20)...

tested_firmware = [
    'TENMA 72-2540 V2.1',
]

class PowerSupply:
    def __init__(self, port):
        self.port = port

    """
    this function is really for internal use... you shouldn't need
    to call it
    """
    def issue_command(self, command, max_response_size=1000):
        if isinstance(command, str):
            command = command.encode('ascii')

        self.port.write(command)
        response = self.port.read(max_response_size)

        return response.rstrip(b'\x00')


    """
    get the power supply's identity string, e.g: "TENMA 72-2540 V2.1"
    """
    def get_identity(self):
        return self.issue_command('*IDN?').decode('ascii')

    """
    check whether the connected power supply has been tested against
    this codebase... when adding new power supplies, please check
    all commands and responses before adding to the tested_firmware
    list
    """
    def is_tested(self):
        identity = self.get_identity()
        return identity in tested_firmware


    def get_status(self):
        response = self.issue_command('STATUS?')
        return pretty_status(response)


    def get_output_state(self):
        return self.get_status().output_enabled

    def set_output_state(self, enabled: bool):
        self.issue_command('OUT1' if enabled else 'OUT0')


    def get_ovp_ocp_state(self):
        return self.get_status().ovp_ocp_enabled

    def set_ocp_state(self, enabled: bool):
        self.issue_command('OCP1' if enabled else 'OCP0')

    def set_ovp_state(self, enabled: bool):
        self.issue_command('OVP1' if enabled else 'OVP0')


    def get_voltage_setpoint(self):
        response = self.issue_command('VSET1?')
        return pretty_reading(response, 'V')

    def set_voltage_setpoint(self, voltage: float):
        self.issue_command('VSET1:%2.2f' % ( voltage ))


    def get_current_setpoint(self):
        response = self.issue_command('ISET1?')
        return pretty_reading(response, 'I')

    def set_current_setpoint(self, current: float):
        self.issue_command('ISET1:%1.3f' % ( current ))


    def get_output_voltage(self):
        response = self.issue_command('VOUT1?')
        return pretty_reading(response, 'V')

    def get_output_current(self):
        response = self.issue_command('IOUT1?')
        return pretty_reading(response, 'I')

    def get_output_readings(self):
        i = self.get_output_current()
        v = self.get_output_voltage()
        p = pretty_reading(i.value * v.value, 'W')
        return i, v, p

    def get_output_power(self):
        return self.get_output_readings()[2]
