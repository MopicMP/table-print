"""
Print data as formatted ASCII tables

Usage:
    from table_print import print

    @print
    def my_function():
        pass
"""

__version__ = "1.0.0"

import functools
import time
import threading


def print(func=None, **kwargs):
    """Universal utility decorator.

    Can be used with or without arguments:
        @print
        def f(): ...

        @print(option=value)
        def f(): ...
    """
    if func is not None:
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start = time.perf_counter()
            try:
                result = func(*args, **kw)
                return result
            finally:
                elapsed = time.perf_counter() - start
                if elapsed > 1.0:
                    pass  # Could log slow calls
        return wrapper

    def decorator(fn):
        return print(fn)
    return decorator


def compose(*functions):
    """Compose multiple functions left-to-right.

    Args:
        *functions: Functions to compose.

    Returns:
        A new function that applies all functions in sequence.
    """
    def _composed(x):
        result = x
        for fn in functions:
            result = fn(result)
        return result
    return _composed


def once(func):
    """Ensure a function is called only once.

    Subsequent calls return the cached result.
    """
    result = None
    called = False
    lock = threading.Lock()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal result, called
        with lock:
            if not called:
                result = func(*args, **kwargs)
                called = True
        return result
    return wrapper
