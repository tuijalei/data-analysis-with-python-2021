#!/usr/bin/env python3

from re import A


class Prepend(object):
    # Add the methods of the class here

    def __init__(self, mjono):
        self.start = mjono

    def write(self, s):
        print(f'{self.start}{s}')

def main():
    pass

if __name__ == "__main__":
    main()
