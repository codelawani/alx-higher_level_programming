#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    string = ''
    for c in text:
        string += c
        if c in '?.:':
            print(string.lstrip(), end='\n\n')
            string = ""
    print(string.lstrip(), end='')
