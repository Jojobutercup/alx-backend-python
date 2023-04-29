#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values
with the appropriate types
"""

from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples containing each element of lst
    and its corresponding length.

    Args:
    - lst: Iterable[Sequence]: a sequence of elements of any type

    Returns:
    - List[Tuple[Sequence, int]]: a list of tuples where each tuple
      contains an element of lst and its corresponding length

    """
    return [(i, len(i)) for i in lst]
