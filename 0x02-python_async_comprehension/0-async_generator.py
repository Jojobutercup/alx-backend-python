#!/usr/bin/env python3

"""
This module contains an asynchronous comprehension
that waits for a random delay
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that yields 10 random numbers
    between 0 and 10, waiting for 1 second between each yield.

    Returns:
        An asynchronous generator that yields floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
