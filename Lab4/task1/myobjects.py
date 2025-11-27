from functools import total_ordering
from smoothsort import smoothsort
from pancakesort import pancake_sort


@total_ordering # класс задаёт правило сравнения, которые будет использовать сортировка
class Student:
    def __init__(self, name: str, grade: float, age: int):
        self.name = name
        self.grade = grade
        self.age = age

    # сортируем по успеваемости (grade), а при равенстве по возрасту
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

    def __repr__(self): # представление объекта в виде строки
        return f"Student({self.name!r}, {self.grade}, {self.age})"


def test_integers():
    data = [6, 4, 7, 1, 5, 8, 9, 17]
    print("Целые, исходный:", data)

    a1 = data.copy()
    smoothsort(a1)
    print("Целые, Smoothsort:", a1)

    a2 = data.copy()
    pancake_sort(a2)
    print("Целые, Pancake:", a2)
    print("-" * 40)


def test_floats():
    data = [3.14, -2.7, 0.0, 10.5, 3.1415]
    print("Вещественные, исходный:", data)

    a1 = data.copy()
    smoothsort(a1)
    print("Вещественные, Smoothsort:", a1)

    a2 = data.copy()
    pancake_sort(a2)
    print("Вещественные, Pancake:", a2)
    print("-" * 40)


def test_strings():
    data = ["banana", "apple", "cherry", "date", "апельсин"]
    print("Строки, исходный:", data)

    a1 = data.copy()
    smoothsort(a1)
    print("Строки, Smoothsort:", a1)

    a2 = data.copy()
    pancake_sort(a2)
    print("Строки, Pancake:", a2)
    print("-" * 40)


def test_students():
    data = [
        Student("Anna", 4.5, 19),
        Student("Boris", 3.7, 20),
        Student("Clara", 4.5, 18),
        Student("Dan", 5.0, 21),
        Student("Eva", 3.7, 19),
    ]
    print("Студенты, исходный:", data)

    a1 = data.copy()
    smoothsort(a1)
    print("Студенты, Smoothsort:", a1)

    a2 = data.copy()
    pancake_sort(a2)
    print("Студенты, Pancake:", a2)
    print("-" * 40)


if __name__ == "__main__":
    test_integers()
    test_floats()
    test_strings()
    test_students()
