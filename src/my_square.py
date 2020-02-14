#!/usr/bin/env python

def my_square(y: int) -> int:
    """
    takes a value and returns the squared value.
    
    Uses the ** infix operator.
    
    :param y: int
    :return: int
    """
    return y ** 2


def my_square2(x: int) -> int:
    return x * x


print(my_square(42))
print(my_square2(42))

