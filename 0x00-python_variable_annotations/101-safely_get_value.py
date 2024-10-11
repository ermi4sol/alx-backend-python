from typing import Mapping, Any, Union, TypeVar

# Define a type variable T
T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    if key in dct:
        return dct[key]
    else:
        return default
