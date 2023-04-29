#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k and the second
    element is the square of v.
    """
    return k, v**2
