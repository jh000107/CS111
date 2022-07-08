def remove_spaces(s):
    """ return a string in which all of the spaces have been removed
        input: s --> string
    """
    if len(s) == 0:
        return s
    else:
        rest_string = remove_spaces(s[1:])
        if s[0] == ' ':
            return rest_string
        else:
            return s[0] + rest_string
