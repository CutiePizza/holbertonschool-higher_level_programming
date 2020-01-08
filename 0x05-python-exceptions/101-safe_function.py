#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        a = fct(*args)
    except Exception as err:
        import sys
        a = None
        print("Exception:", err, file=sys.stderr)
    return a
