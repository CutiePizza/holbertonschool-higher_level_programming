#!/usr/bin/python3
class MyList(list):

    def print_sorted(self):
        print(sorted(self))

    def __str__(self):
        return str(list(self))
