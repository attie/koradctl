# Korad Control

A simple python library to support the control and automation of Korad KAxxxxP series power supplies.
These supplies are also rebadged as other brands including Tenma and Vellerman.

- [Command Reference](https://sigrok.org/wiki/Korad_KAxxxxP_series)

## Setup

```bash
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
# Output off
python3 -m koradctl -e off

# 12v, 400mA, Output on, Monitor with readings once every 10 seconds
python3 -m koradctl -v 12 -i 0.4 -e on -M -f 10

# 3.3v, 250mA, OCP on, OVP off, Output on, Monitor once
python3 -m koradctl --ocp on --ovp off -v 3.3 -i 0.25 -e on -m
```

## Power Supply API

- Misc
    - `get_identity()`
    - `is_tested()`
    - `get_status()`
- Output State
    - `get_output_state()`
    - `set_output_state(enabled)`
- Voltage and Over Current Protection
    - `get_ovp_ocp_state()`
    - `set_ocp_state(enabled)`
    - `set_ovp_state(enabled)`
- Setpoint Control
    - Voltage
        - `get_voltage_setpoint()`
        - `set_voltage_setpoint(voltage)`
    - Current
        - `get_current_setpoint()`
        - `set_current_setpoint(current)`
- Output Readings
    - `get_output_voltage()`
    - `get_output_current()`
    - `get_output_power()`
    - `get_output_readings()`
