#!/usr/bin/env python3
from typing import Sequence, Any, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence from which to get the first element.

    Returns:
        Optional[Any]: The first element of the sequence or None if empty.
    """
    if lst:
        return lst[0]
    else:
        return None
