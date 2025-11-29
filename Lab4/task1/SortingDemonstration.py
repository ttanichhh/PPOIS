from SmoothSorter import SmoothSorter
from PancakeSorter import PancakeSorter
from Student import Student


class SortingDemonstration:
    def __init__(self):
        self.smooth_sorter = SmoothSorter()
        self.pancake_sorter = PancakeSorter()

    def test_integers(self):
        data = [6, 4, 7, 1, 5, 8, 9, 17]
        print("Целые, исходный:", data)

        a1 = data.copy()
        self.smooth_sorter.sort(a1)
        print("Целые, Smoothsort:", a1)

        a2 = data.copy()
        self.pancake_sorter.sort(a2)
        print("Целые, Pancake:", a2)
        print("-" * 40)

    def test_floats(self):
        data = [3.14, -2.7, 0.0, 10.5, 3.1415]
        print("Вещественные, исходный:", data)

        a1 = data.copy()
        self.smooth_sorter.sort(a1)
        print("Вещественные, Smoothsort:", a1)

        a2 = data.copy()
        self.pancake_sorter.sort(a2)
        print("Вещественные, Pancake:", a2)
        print("-" * 40)

    def test_strings(self):
        data = ["banana", "apple", "cherry", "date", "апельсин"]
        print("Строки, исходный:", data)

        a1 = data.copy()
        self.smooth_sorter.sort(a1)
        print("Строки, Smoothsort:", a1)

        a2 = data.copy()
        self.pancake_sorter.sort(a2)
        print("Строки, Pancake:", a2)
        print("-" * 40)

    def test_students(self):
        data = [
            Student("Anna", 4.5, 19),
            Student("Boris", 3.7, 20),
            Student("Clara", 4.5, 18),
            Student("Dan", 5.0, 21),
            Student("Eva", 3.7, 19),
        ]
        print("Студенты, исходный:", data)

        a1 = data.copy()
        self.smooth_sorter.sort(a1)
        print("Студенты, Smoothsort:", a1)

        a2 = data.copy()
        self.pancake_sorter.sort(a2)
        print("Студенты, Pancake:", a2)
        print("-" * 40)

    def run_all_tests(self):
        """Запускает все тесты."""
        self.test_integers()
        self.test_floats()
        self.test_strings()
        self.test_students()


if __name__ == "__main__":
    tester = SortingDemonstration()
    tester.run_all_tests()