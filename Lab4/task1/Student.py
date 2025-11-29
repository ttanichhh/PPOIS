from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name: str, grade: float, age: int):
        self.name = name
        self.grade = grade
        self.age = age

    def __lt__(self, other):
        if self.grade == other.grade:
            return self.age < other.age
        return self.grade < other.grade

    def __eq__(self, other):
        return (
                self.grade == other.grade
                and self.age == other.age
                and self.name == other.name
        )

    def __repr__(self):
        return f"Student({self.name!r}, {self.grade}, {self.age})"