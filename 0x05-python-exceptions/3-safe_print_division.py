#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        answer = a / b
    except (ZeroDivisionError, TypeError):
        answer = None
    finally:
        return ("Inside result: {}".format(answer))
    return (answer)