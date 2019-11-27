from time import sleep

from koradctl.port import get_port
from koradctl.psu import PowerSupply

port = get_port('/dev/ttyACM0')
psu = PowerSupply(port)

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
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    psu.set_output_state(False)
