#!/usr/bin/python3
def append_write(filename="", text=""):
    ''' that appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    '''
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
