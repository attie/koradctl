from typing import Union
from collections import namedtuple

status_fields = {
    'output_enabled':  lambda x: bool( x & 0x40),
    'ovp_ocp_enabled': lambda x: bool( x & 0x80),
    'cv_active':       lambda x: bool( x & 0x01),
    'cc_active':       lambda x: bool(~x & 0x01),
}
Status = namedtuple('Status', status_fields.keys())

def pretty_status(response: bytes):
    status_byte = response[0]
    d = { k: fn(status_byte) for k,fn in status_fields.items() }
    return Status(**d)


reading_fields = {
    'value': lambda x,y: round(float(x), 3),
    'units': lambda x,y: y,
}
Reading = namedtuple('Reading', reading_fields.keys())

def pretty_reading(response: Union[bytes, float], units: str = '?'):
    d = { k: fn(response, units) for k,fn in reading_fields.items() }
    return Reading(**d)
