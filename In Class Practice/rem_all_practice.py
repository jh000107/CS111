def rem_all(element, values):
    if values == []:
        return []
    else:
        rest = rem_all(element, values[1:])
        if values[0] == element:
            return rest
        else:
            return values[0] + rest

print(rem_all(10, [10, 3, 4]))

            
        
