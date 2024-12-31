from __future__ import annotations

from typing import Union
from typing import NamedTuple

class Status(NamedTuple):
    output_enabled: bool
    ovp_ocp_enabled: bool
    cv_active: bool
    cc_active: bool

    @staticmethod
    def from_status_byte(status_byte: int) -> Status:
        assert 0 <= status_byte <= 255
        return Status(
            output_enabled=bool(status_byte & 0x40),
            ovp_ocp_enabled=bool(status_byte & 0x80),
            cv_active=bool(status_byte & 0x01),
            cc_active=bool(~status_byte & 0x01),
        )

def pretty_status(response: bytes) -> Status:
    status_byte = response[0]
    return Status.from_status_byte(status_byte)

class Reading(NamedTuple):
    value: float
    units: str

def pretty_reading(response: Union[bytes, float], units: str = '?'):
    return Reading(
        value = round(float(response), 3),
        units = units
    )
