#!/usr/bin/env python

from time import sleep
from serial.serialutil import SerialException

import koradctl

"""
more complex example script
try connecting a resistive load, for example 2.5 Ohms and watch the output
try connecting a device with a SMPS (that can handle the voltage) and watch the output

steps:
- set the output to V_START
- set the current limit to 2A
- enable over-current protection after 250ms
- adjust the voltage setpoint by V_STEP, every 250ms, aiming for V_END
"""

V_START = 0
V_END = 12
V_STEP = 0.5

def get_next_voltage(v_live):
    if v_live == V_END:
        raise StopIteration()

    if v_live < V_END:
        v_next = v_live + V_STEP
    else:
        v_next = v_live - V_STEP
    return v_next

port = koradctl.get_port('/dev/ttyACM0')
psu = koradctl.PowerSupply(port)

# disable OCP / OVP
psu.set_ocp_state(False)
psu.set_ovp_state(False)

# setup output
psu.set_voltage_setpoint(V_START)
psu.set_current_setpoint(2)

# enable output
psu.set_output_state(True)

# wait for startup, and then enable OCP
sleep(0.25)
psu.set_ocp_state(True)

try:
    # log power usage at ~1Hz
    while True:
        i, v, p = psu.get_output_readings()
        print('%2.2fv    %1.3fA    %2.2fW' % ( v.value, i.value, p.value ))

        if not psu.get_output_state():
            # if the output is no longer enabled, then exit
            # this could happen if the OCP kicked in
            break

        v_next = get_next_voltage(v.value)
        if v_next is not None:
            psu.set_voltage_setpoint(v_next)

        sleep(0.25)
except ( KeyboardInterrupt, StopIteration ):
    pass
except SerialException:
    print('ERROR: The power supply appears to have gone away...', file=sys.stderr)
finally:
    psu.set_output_state(False)
