#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception
try:
    raise_exception()
except TypeError:
    print("Exception has been raised")
