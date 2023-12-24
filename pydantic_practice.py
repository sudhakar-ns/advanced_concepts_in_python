from typing import Any, Callable
from benedict import BeneDict
from pydantic import BaseModel, field_validator, ValidationError
from pydantic_core.core_schema import FieldValidationInfo


class StaticList(BaseModel):
    nums: list
    
    @staticmethod
    def check_list_types(lst):
        if not lst:  return True
        first_type = type(lst[0])
        return all(type(element) == first_type for element in lst)

    @field_validator('nums')
    def validate_type[T](cls, v: list[T | Any], _: FieldValidationInfo) -> list[T]:
        # print(f"infos: {info}")
        if not StaticList.check_list_types(v): raise ValueError("Types are not static, sorry Bruh!")
        return v


def sort_list[T](_list: T) -> list[T]:
    return sorted(_list)

if __name__ == '__main__':
    try:
        nums = StaticList(nums=[10, 2, 2, 4, 's'])
        print(sort_list(nums.nums))
    except ValidationError as err: print(err.json(indent=2))