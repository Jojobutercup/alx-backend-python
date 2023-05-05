#!/usr/bin/env python3
"""
Module: 4-tasks.
------------------------

This module contains an asynchronous coroutine:
task_wait_random.

"""

import asyncio
import random
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Wait for a random delay between 0 and max_delay seconds and return
    a list of them.
    """
    tasks = [
        asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)
    ]
    return [await task for task in asyncio.as_completed(tasks)]
