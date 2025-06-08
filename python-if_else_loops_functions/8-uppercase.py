#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += "{:c}".format(ord(char) - 32)
        else:
            result += char
    print(result)
