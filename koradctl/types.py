true_values = [ '1', 'on', 'yes' ]
false_values = [ '0', 'off', 'no' ]
toggle_values = [ 't', 'toggle' ]

def human_bool(arg: str):
    if arg in true_values:
        return True
    if arg in false_values:
        return False

    raise TypeError('Must be a "human" boolean (one of: %s)' % ( [ *true_values, *false_values ] ))

def human_bool_toggle(arg: str):
    if arg in true_values:
        return True
    if arg in false_values:
        return False
    if arg in toggle_values:
        return 'toggle'

    raise TypeError('Must be a "human" boolean, or toggle (one of: %s)' % ( [ *true_values, *false_values, *toggle_values ]))
