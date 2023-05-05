#!/usr/bin/env python3
"""
An async comprehension that collects 10 random
numbers from async_generator.
"""
from asyncio import gather
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers
    using an async comprehension over the async_generator
    coroutine.

    Returns:
        A list of 10 random floats.
    """
    return [x async for x in async_generator()][:10]
