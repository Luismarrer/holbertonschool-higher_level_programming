#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except IndexError as e:
        print("Exception: {}" .format(e), file=sys.stderr)
        return None
    except ZeroDivisionError as e:
        print("Exception: {}" .format(e), file=sys.stderr)
        return None
