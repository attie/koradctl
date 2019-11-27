from time import sleep
from serial.serialutil import SerialException

import koradctl

"""
basic example script
- set the output to 12v
- set the current limit to 0.5v
- enable over-current protection after 250ms
"""

port = koradctl.get_port('/dev/ttyACM0')
psu = koradctl.PowerSupply(port)

# disable OCP / OVP
psu.set_ocp_state(False)
psu.set_ovp_state(False)

# setup output
psu.set_voltage_setpoint(12)
psu.set_current_setpoint(0.5)

# enable output
psu.set_output_state(True)

# wait for startup, and then enable OCP
sleep(0.25)
psu.set_ocp_state(True)

try:
    # log power usage at ~1Hz
    while True:
        v = psu.get_output_voltage().value
        i = psu.get_output_current().value
        p = psu.get_output_power().value
        print('%2.2fv    %1.3fA    %2.2fW' % ( v, i, p ))

        if not psu.get_output_state():
            # if the output is no longer enabled, then exit
            # this could happen if the OCP kicked in
            break

        sleep(1)
except KeyboardInterrupt:
    pass
except SerialException:
    print('ERROR: The power supply appears to have gone away...', file=sys.stderr)
finally:
    psu.set_output_state(False)
