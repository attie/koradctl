true_values = [ '1', 'on', 'yes' ]
false_values = [ '0', 'off', 'no' ]
toggle_values = [ 't', 'toggle' ]

def from_options(arg: str, options: list):
    for values, ret in options:
        if arg in values:
            return ret

    raise TypeError('Must be one of: %s' % ( [ i for s in options for i in s[0] ] ))

def human_bool(arg: str):
    return from_options(arg, [
        ( true_values,  True  ),
        ( false_values, False ),
    ])

def human_bool_toggle(arg: str):
    return from_options(arg, [
        ( true_values,   True     ),
        ( false_values,  False    ),
        ( toggle_values, 'toggle' ),
    ])
