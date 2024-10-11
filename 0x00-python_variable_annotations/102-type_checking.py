#!/usr/bin/env python3
from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """Creates a new list by repeating each element of the input list a specified number of times.

    Args:
        lst (Tuple[int, ...]): The input tuple of integers.
        factor (int, optional): The number of times to repeat each element. Defaults to 2.

    Returns:
        List[int]: A list containing the elements of lst, each repeated factor times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

# Example usage
array: Tuple[int, ...] = (12, 72, 91)

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
