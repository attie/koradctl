def human_bool(arg: str):
    true_values = [ '1', 'on', 'yes' ]
    false_values = [ '0', 'off', 'no' ]

    if arg in true_values:
        return True
    if arg in false_values:
        return False

    raise TypeError('Must be a "human" boolean (one of: %s)' % ( [ *true_values, *false_values ] ))
