"""
Test solid principles
"""
import math
import abc
import json

class ShapeMetaClass(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'area') and callable(subclass.area))


class ShapeInterface(metaclass=abc.ABCMeta):
    """
    Open-Closed Principle
    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'area') and callable(subclass.area))


class ManageInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'calculate') and callable(subclass.calculate))


class ThreeDShapesInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'area') and callable(subclass.area) and hasattr(subclass, 'volume') and callable(subclass.volume))


class Square(ShapeInterface, ManageInterface):
    def __init__(self, length):
        self.length = length

    def area(self):
        return math.pow(self.length, 2)

    def calculate(self):
        return self.area()


class Circle(ShapeInterface, ManageInterface):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def calculate(self):
        return self.area()


class Cuboid(ShapeInterface, ThreeDShapesInterface):
    def area(self):
        pass

    def volume(self):
        pass

    def calculate(self):
        return self.area()


class AreaCalculator():
    def __init__(self, shapes: list):
        self.shapes = shapes

    def sum_areas(self):
        areas = []

        for shape in self.shapes:
            areas.append(round(shape.calculate(), 2))
        return sum(areas)

class VolumeCalculator(AreaCalculator):
    def __init__(self, shapes):
        super(AreaCalculator, self).__init__(shapes)

    def sum_volumes(self):
        volumes = []

#         for shape in self.shapes:
#             volumes.append(shape.area())
        return volumes


class SumCalculatorOutputter(AreaCalculator):
    def __init__(self, shapes):
        super().__init__(shapes)

    def to_json(self):
        data = {
                'sum': self.sum_areas()
                }
        return json.dumps(data)

    def html(self):
        return f'Sum of the areas of the shapes is {self.sum_areas()}'


if __name__ == '__main__':
    s = Square(8)
    c = Circle(7)

    ac = SumCalculatorOutputter([s, c])
    print(ac.to_json())
    print(ac.html())

