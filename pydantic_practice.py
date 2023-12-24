from typing import Any

from pydantic import BaseModel, ValidationError, field_validator
from pydantic_core.core_schema import FieldValidationInfo

__name__ = 'Pydantic Library basic implementation'
__author__ = 'Sudhakar N S'
__doc__ = """
    This files comprises of basic data validation implementation using pydantic module.
"""

class StaticList(BaseModel):
    """
        This class is a model which gets list of elements as input, validates the types and sets it.
        If the list is of dynamic types, it throws a validation error.
        Since Python is dynamically types, ultimately this happens at runtime only.

        Args:
            BaseModel (_type_): BaseModel from pydantic

        Raises:
            ValueError: ValidationError if condition does not satisfy

        Returns:
            _type_: None
    """
    nums: list
    
    @staticmethod
    def check_list_types(lst):
        if not lst:  return True
        first_type = type(lst[0])
        return all(type(element) == first_type for element in lst)

    @field_validator('nums')
    def validate_type[T](cls, v: list[T | Any], info: FieldValidationInfo) -> list[T]:
        print(f"infos: {info}")
        if not StaticList.check_list_types(v): raise ValueError("Types are not static, sorry Bruh!")
        return v

if __name__ == '__main__':
    try:
        nums = StaticList(nums=[10, 2, 2, 4, 5]) # This will work successfully | nums = [10, 2, 2, 4, 5]
        nums = StaticList(nums=[10, 2, 2, 4, 'a']) # This will not work | Value error, Types are not static, sorry Bruh! [type=value_error, input_value=[10, 2, 2, 4, 'a'], input_type=list]
    except ValidationError as err: print(err.json(indent=2))