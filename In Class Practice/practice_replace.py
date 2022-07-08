def replace(s, old, new):
    if s == '':
        return ''
    else:
        repl_rest = replace(s[1:], old, new)
        if s[0] == old:
           return new + repl_rest
        else:
            return s[0] + repl_rest

print(replace('hello', 'l', 'x'))
