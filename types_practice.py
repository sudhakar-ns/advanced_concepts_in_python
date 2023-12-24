from typing import Callable, TypeVar

_T = TypeVar('_T')

def sort_list[T](_list: T) -> list[T]:
    return sorted(_list)


if __name__ == '__main__':
    return_list: Callable[[_T], _T] = lambda x: x