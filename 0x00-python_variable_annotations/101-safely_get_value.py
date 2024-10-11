#!/usr/bin/env python3
from typing import Mapping, Any, Optional, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """Retrieves a value from a dictionary safely.

    Args:
        dct (Mapping[Any, T]): The dictionary from which to retrieve the value.
        key (Any): The key whose value needs to be retrieved.
        default (Optional[T], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Optional[T]: The value associated with the key or the default value if not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
