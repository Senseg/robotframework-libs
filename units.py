"""Helper routine to parse numbers with units."""

import re

def parse_unit(s, expected_unit=None, unit_required=False):
    muls = { None: 1.0, 'k': 1000.0, 'm': 1.0/1000, 'u': 1.0/1000000, 'n': 1.0/1000000000 }
    m = re.match(r'([0-9\.eE+-]+) *(k|m|u|n)?(s|discharger_clocks|cycles|Hz|%|V)?', s)
    if not m:
        raise RuntimeError("not a number + unit: " + s)
    (value, prefix, unit) = m.groups()
    if expected_unit:
        if unit or unit_required:
            if expected_unit != unit:
                raise RuntimeError("Expecting unit " + expected_unit + ", found unit " + unit)
    return (float(value) * muls[prefix], unit)

