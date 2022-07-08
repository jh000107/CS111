def remove_vowels(s):
    if s == '':
        return ''
    else:
        rem_rest = remove_vowels(s[1:])
        if s[0] in 'aeiou':
            return rem_rest
        else:
            return s[0] + rem_rest

