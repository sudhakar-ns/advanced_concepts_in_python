from dataclasses import dataclass
from typing import Callable, Generic, TypeAlias, TypeVar

__name__ = 'Python Types'
__author__ = 'Sudhakar N S'
__doc__ = """
    This file comprises of basic implementations of python generics.
    There are two ways of using generics. 
    Python prior to 3.12 uses TypeVar which is present in typing module. Python 3.12 uses a syntax similar to other languages such as Typescript 'func_name[T](arg: T) -> T:'
"""

## Before Python 3.12

T = TypeVar('T')  # T is a generic type variable

process_numbers_lambda: Callable[[T], T] = lambda x: [ele for ind, ele in enumerate(x) if ind % 2 == 1]

# A non-generic type alias
IntOrStr = int | str

# A generic type alias
ListOrSet: TypeAlias = list[T] | set[T]


class Box(Generic[T]):
    def __init__(self, item: T):
        self.item = item
    
    def get_item(self) -> T:
        return self.item
    
    def set_item(self, new_item: T) -> None:
        self.item = new_item

# A generic function example
def get_first_item(items: list[T]) -> T:
    return items[0]

def box() -> None:
    int_box = Box(123)  # Integer Box
    int_item = int_box.get_item()
    print(int_item)  # Output: 123

    str_box = Box("Hello, Generics!")  # String Box
    str_item = str_box.get_item()
    print(str_item)  # Output: Hello, Generics!

    list_box = Box([1, 2, 3])  # List Box
    list_item = list_box.get_item()
    print(list_item)  # Output: [1, 2, 3]

    first_item = get_first_item([1, 2, 3])  # Generic function
    print(first_item)  # Output: 1


# Define a base class named Vehicle
@dataclass
class Vehicle:
    model: str

    def display(self) -> None:
        print(f"Vehicle model: {self.model}")

# Define two subclasses for Vehicle: Car and Boat
class Car(Vehicle):
    def display(self) -> None:
        print(f"Car model: {self.model}")

class Boat(Vehicle):
    def display(self) -> None:
        print(f"Boat model: {self.model}")


# Create a TypeVar with an upper bound of Vehicle
V = TypeVar("V", bound=Vehicle)

class VehicleRegistry(Generic[V]):
    def __init__(self) -> None:
        self.vehicles: list[V] = []

    def add_vehicle(self, vehicle: V) -> None:
        self.vehicles.append(vehicle)
    
    def display_all(self) -> None:
        for vehicle in self.vehicles:
            vehicle.display()


def vehicle_before() -> None:
    # Usage
    registry = VehicleRegistry[Car]()
    registry.add_vehicle(Car("Sedan"))
    registry.add_vehicle(Car("SUV"))
    registry.display_all()

    # This will raise a type error
    # registry.add_vehicle(Boat("Yacht"))

    # If you need a registry that accepts any kind of Vehicle (or its subclasses)
    generic_registry = VehicleRegistry[Vehicle]()
    generic_registry.add_vehicle(Car("Convertible"))
    generic_registry.add_vehicle(Boat("Cruiser"))
    generic_registry.display_all()



## After Python 3.12

# A non-generic type alias
type IntOrStr = int | str

# A generic type alias
type _ListOrSet[T] = list[T] | set[T]

class Box[T]:
    def __init__(self, item: T):
        self.item = item
    
    def get_item(self) -> T:
        return self.item
    
    def set_item(self, new_item: T) -> None:
        self.item = new_item

# A generic function example
def get_first_item[T](items: list[T]) -> T:
    return items[0]


# Define a base class named Vehicle
@dataclass
class Vehicle:
    model: str

    def display(self) -> None:
        print(f"Vehicle model: {self.model}")


# Define two subclasses for Vehicle: Car and Boat
class Car(Vehicle):
    def display(self) -> None:
        print(f"Car model: {self.model}")


class Boat(Vehicle):
    def display(self) -> None:
        print(f"Boat model: {self.model}")

class Plane(Vehicle):
    def display(self) -> None:
        print(f"Plane model: {self.model}")
        
class VehicleRegistry[V: Vehicle]:
    def __init__(self) -> None:
        self.vehicles: list[V] = []

    def add_vehicle(self, vehicle: V) -> None:
        self.vehicles.append(vehicle)

    def display_all(self) -> None:
        for vehicle in self.vehicles:
            vehicle.display()


def vehicle_after() -> None:
    # Usage
    registry = VehicleRegistry[Car]()
    registry.add_vehicle(Car("Sedan"))
    registry.add_vehicle(Car("SUV"))
    registry.display_all()

    # This will raise a type error
    # registry.add_vehicle(Boat("Yacht"))

    # If you need a registry that accepts any kind of Vehicle (or its subclasses)
    generic_registry = VehicleRegistry[Vehicle]()
    generic_registry.add_vehicle(Car("Convertible"))
    generic_registry.add_vehicle(Boat("Cruiser"))
    generic_registry.display_all()