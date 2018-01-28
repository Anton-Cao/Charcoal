def conv(i):
    '''
    Maps a character to a number and vice versa
    '''
    if type(i) == str:
        d = {
            ' ' : 26,
            '.' : 27,
            ',' : 28
        }

        if i.isalpha():
            return ord(i.lower()) - ord('a')
        elif i in d:
            return d[i]
        else:
            return 29
    else:
        if i <= ord('z') - ord('a'):
            return chr(i + ord('a'))
        elif i == 26:
            return " "
        elif i == 27:
            return "."
        elif i == 28:
            return ","
        else:
            return "*"

num_previous = 10
