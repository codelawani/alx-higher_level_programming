#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    string = ''
    for i in range(len(text)):
        if text[i] == ' ' and (text[i - 1] == '.' or text[i - 1] == ':' or text[i - 1] == '?'):
            continue
        string += text[i]
    for c in string:
        print(c, end='\n\n' if c == '.' or c == '?' or c == ':' else '')
