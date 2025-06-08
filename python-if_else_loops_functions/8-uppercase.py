#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print("{:c}".format(ord(char)), end="")
    print()
