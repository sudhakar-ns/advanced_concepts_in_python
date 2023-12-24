from typing import Callable, TypeVar

__name__ = 'Python Types'
__author__ = 'Sudhakar N S'
__doc__ = """
    This file comprises of basic implementations of python generics.
    There are two ways of using generics. 
    Python prior to 3.12 uses TypeVar which is present in typing module. Python 3.12 uses a syntax similar to other languages such as Typescript 'func_name[T](arg: T) -> T:'
"""

_T = TypeVar('_T')

def sort_list[T](_list: T) -> list[T]:
    """
    This function is used to sort the input list and return it.
    Generics is used here [T].

    Args:
        _list: List of elements

    Returns:
        _type_: a sorted list [T]
    """
    return sorted(_list)


if __name__ == '__main__':
    return_list: Callable[[_T], _T] = lambda x: x