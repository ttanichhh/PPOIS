import random
from enum import Enum
from typing import List


class Color(Enum):
    WHITE = 0
    YELLOW = 1
    RED = 2
    ORANGE = 3
    GREEN = 4
    BLUE = 5
    NONE = 6


class RubiksCube:
    # создать кубик Рубика с начальными цветами
    def __init__(self):
        self.front = [[Color.RED for _ in range(3)] for _ in range(3)]
        self.back = [[Color.ORANGE for _ in range(3)] for _ in range(3)]
        self.left = [[Color.GREEN for _ in range(3)] for _ in range(3)]
        self.right = [[Color.BLUE for _ in range(3)] for _ in range(3)]
        self.up = [[Color.WHITE for _ in range(3)] for _ in range(3)]
        self.down = [[Color.YELLOW for _ in range(3)] for _ in range(3)]
        self.initialize()

    # сбросить кубик в собранное состояние
    def initialize(self):
        """Инициализация собранного куба"""
        for i in range(3):
            for j in range(3):
                self.front[i][j] = Color.RED
                self.back[i][j] = Color.ORANGE
                self.left[i][j] = Color.GREEN
                self.right[i][j] = Color.BLUE
                self.up[i][j] = Color.WHITE
                self.down[i][j] = Color.YELLOW

    # повернуть одну грань на 90° по часовой
    def rotate_face_clockwise(self, face: List[List[Color]]):
        """Поворот грани по часовой стрелке"""
        temp = [row[:] for row in face]
        for i in range(3):
            for j in range(3):
                face[i][j] = temp[2 - j][i]
    '''
    1  2  3    7  4  1
    4  5  6    8  5  2
    7  8  9    3  2  1
    '''

    # повернуть одну грань на 90° против часовой
    def rotate_face_counter_clockwise(self, face: List[List[Color]]):
        """Поворот грани против часовой стрелки"""
        temp = [row[:] for row in face] # полная независимая копия исходной грани,
                                        # чтобы брать значения из старой матрицы, не перезаписываю результат
        for i in range(3): # новые строки (0,1,2)
            for j in range(3): # новые столбцы (0,1,2)
                face[i][j] = temp[j][2 - i]
    '''
    1  2  3    3  6  9
    4  5  6    2  5  8
    7  8  9    1  4  7
    '''

    # Front повернуть по часовой
    def rotate_front_clockwise(self):
        """Поворот передней грани по часовой стрелке"""
        self.rotate_face_clockwise(self.front) # переворачивает только центральную грань

        # Сохраняем верхний ряд верхней грани (который примыкает к передней грани):
        temp = self.up[2][:] #( [:] создает копию списка начала до конца)

        # Перемещаем элементы
        for i in range(3):
            self.up[2][i] = self.left[2 - i][2]
            self.left[2 - i][2] = self.down[0][2 - i]
            self.down[0][2 - i] = self.right[i][0]
            self.right[i][0] = temp[i]

    # Front повернуть против часовой
    def rotate_front_counter_clockwise(self):
        """Поворот передней грани против часовой стрелки"""
        self.rotate_face_counter_clockwise(self.front)

        temp = self.up[2][:]

        for i in range(3):
            self.up[2][i] = self.right[i][0]
            self.right[i][0] = self.down[0][2 - i]
            self.down[0][2 - i] = self.left[2 - i][2]
            self.left[2 - i][2] = temp[i]

    # Right повернуть по часовой
    def rotate_right_clockwise(self):
        """Поворот правой грани по часовой стрелке"""
        self.rotate_face_clockwise(self.right)

        temp = [self.up[i][2] for i in range(3)]

        for i in range(3):
            self.up[i][2] = self.front[i][2]
            self.front[i][2] = self.down[i][2]
            self.down[i][2] = self.back[2 - i][0]
            self.back[2 - i][0] = temp[i]

    # Right повернуть против часовой
    def rotate_right_counter_clockwise(self):
        """Поворот правой грани против часовой стрелки"""
        self.rotate_face_counter_clockwise(self.right)

        temp = [self.up[i][2] for i in range(3)]

        for i in range(3):
            self.up[i][2] = self.back[2 - i][0]
            self.back[2 - i][0] = self.down[i][2]
            self.down[i][2] = self.front[i][2]
            self.front[i][2] = temp[i]

    # Left повернуть по часовой
    def rotate_left_clockwise(self):
        """Поворот левой грани по часовой стрелке"""
        self.rotate_face_clockwise(self.left)

        temp = [self.up[i][0] for i in range(3)]

        for i in range(3):
            self.up[i][0] = self.back[2 - i][2]
            self.back[2 - i][2] = self.down[i][0]
            self.down[i][0] = self.front[i][0]
            self.front[i][0] = temp[i]

    # Left повернуть против часовой
    def rotate_left_counter_clockwise(self):
        """Поворот левой грани против часовой стрелки"""
        self.rotate_face_counter_clockwise(self.left)

        temp = [self.up[i][0] for i in range(3)]

        for i in range(3):
            self.up[i][0] = self.front[i][0]
            self.front[i][0] = self.down[i][0]
            self.down[i][0] = self.back[2 - i][2]
            self.back[2 - i][2] = temp[i]

    # Up повернуть по часовой
    def rotate_up_clockwise(self):
        """Поворот верхней грани по часовой стрелке"""
        self.rotate_face_clockwise(self.up)

        temp = self.front[0][:]

        for i in range(3):
            self.front[0][i] = self.right[0][i]
            self.right[0][i] = self.back[0][i]
            self.back[0][i] = self.left[0][i]
            self.left[0][i] = temp[i]

    # Up повернуть против часовой
    def rotate_up_counter_clockwise(self):
        """Поворот верхней грани против часовой стрелки"""
        self.rotate_face_counter_clockwise(self.up)

        temp = self.front[0][:]

        for i in range(3):
            self.front[0][i] = self.left[0][i]
            self.left[0][i] = self.back[0][i]
            self.back[0][i] = self.right[0][i]
            self.right[0][i] = temp[i]

    # Down повернуть по часовой
    def rotate_down_clockwise(self):
        """Поворот нижней грани по часовой стрелке"""
        self.rotate_face_clockwise(self.down)

        temp = self.front[2][:]

        for i in range(3):
            self.front[2][i] = self.left[2][i]
            self.left[2][i] = self.back[2][i]
            self.back[2][i] = self.right[2][i]
            self.right[2][i] = temp[i]

    # Down повернуть против часовой
    def rotate_down_counter_clockwise(self):
        """Поворот нижней грани против часовой стрелки"""
        self.rotate_face_counter_clockwise(self.down)

        temp = self.front[2][:]

        for i in range(3):
            self.front[2][i] = self.right[2][i]
            self.right[2][i] = self.back[2][i]
            self.back[2][i] = self.left[2][i]
            self.left[2][i] = temp[i]

    # Back повернуть по часовой
    def rotate_back_clockwise(self):
        """Поворот задней грани по часовой стрелке"""
        self.rotate_face_clockwise(self.back)

        temp = self.up[0][:]

        for i in range(3):
            self.up[0][i] = self.right[i][2]
            self.right[i][2] = self.down[2][2 - i]
            self.down[2][2 - i] = self.left[2 - i][0]
            self.left[2 - i][0] = temp[i]

    # Back повернуть против часовой
    def rotate_back_counter_clockwise(self):
        """Поворот задней грани против часовой стрелки"""
        self.rotate_face_counter_clockwise(self.back)

        temp = self.up[0][:]

        for i in range(3):
            self.up[0][i] = self.left[2 - i][0]
            self.left[2 - i][0] = self.down[2][2 - i]
            self.down[2][2 - i] = self.right[i][2]
            self.right[i][2] = temp[i]

    def scramble(self, moves=20):
        """Перемешивание куба"""
        rotations = [
            self.rotate_front_clockwise,
            self.rotate_front_counter_clockwise,
            self.rotate_right_clockwise,
            self.rotate_right_counter_clockwise,
            self.rotate_left_clockwise,
            self.rotate_left_counter_clockwise,
            self.rotate_up_clockwise,
            self.rotate_up_counter_clockwise,
            self.rotate_down_clockwise,
            self.rotate_down_counter_clockwise,
            self.rotate_back_clockwise,
            self.rotate_back_counter_clockwise
        ]

        for _ in range(moves):
            rotation_func = random.choice(rotations)
            rotation_func()

    def is_solved(self):
        """Проверка, собран ли куб"""
        return (self.is_face_uniform(self.front) and
                self.is_face_uniform(self.back) and
                self.is_face_uniform(self.left) and
                self.is_face_uniform(self.right) and
                self.is_face_uniform(self.up) and
                self.is_face_uniform(self.down))


    def is_face_uniform(self, face):
        """Проверка, что грань одноцветна"""
        first_color = face[0][0]
        for row in face:
            for color in row:
                if color != first_color:
                    return False
        return True

    def display(self):
        """Вывод куба в консоль"""
        print("Кубик-рубик:\n")

        # Верхняя грань
        print("Вверх(белый):")
        self.print_face(self.up)
        print("\n")

        # Средний слой
        print("Середина:")
        for i in range(3):
            print("  ", end="")
            self.print_row(self.left[i])
            print(" ", end="")
            self.print_row(self.front[i])
            print(" ", end="")
            self.print_row(self.right[i])
            print(" ", end="")
            self.print_row(self.back[i])
            print()
        print("\n")

        # Нижняя грань
        print("Низ(желтый):")
        self.print_face(self.down)

    def print_row(self, row):
        """Вывод строки грани"""
        for color in row:
            print(self.color_to_char(color), end=" ")

    def print_face(self, face):
        """Вывод всей грани"""
        for row in face:
            print("  ", end="")
            self.print_row(row)
            print()

    def color_to_char(self, color):
        """Преобразование цвета в символ"""
        if color == Color.WHITE:
            return 'W'
        elif color == Color.YELLOW:
            return 'Y'
        elif color == Color.RED:
            return 'R'
        elif color == Color.ORANGE:
            return 'O'
        elif color == Color.GREEN:
            return 'G'
        elif color == Color.BLUE:
            return 'B'
        else:
            return ' '


def main():
    cube = RubiksCube()

    while True:
        print("\n" + "=" * 40)
        print("        КУБИК РУБИКА")
        print("=" * 40)
        print("1. Показать кубик")
        print("2. Повернуть переднюю грань по часовой")
        print("3. Повернуть переднюю грань против часовой")
        print("4. Повернуть правую грань по часовой")
        print("5. Повернуть правую грань против часовой")
        print("6. Повернуть левую грань по часовой")
        print("7. Повернуть левую грань против часовой")
        print("8. Повернуть верхнюю грань по часовой")
        print("9. Повернуть верхнюю грань против часовой")
        print("10. Повернуть нижнюю грань по часовой")
        print("11. Повернуть нижнюю грань против часовой")
        print("12. Повернуть заднюю грань по часовой")
        print("13. Повернуть заднюю грань против часовой")
        print("14. Перемешать кубик")
        print("15. Проверить, решено ли")
        print("16. Вернуть на свои места")
        print("0. ВЫЙТИ")
        print("=" * 40)

        try:
            choice = int(input("Выберите опцию: "))
        except ValueError:
            print("Пожалуйста, введите число!")
            continue

        if choice == 0:
            print("До свидания!")
            break
        elif choice == 1:
            cube.display()
        elif choice == 2:
            cube.rotate_front_clockwise()
            print("Передняя грань повернута по часовой стрелке")
        elif choice == 3:
            cube.rotate_front_counter_clockwise()
            print("Передняя грань повернута против часовой стрелки")
        elif choice == 4:
            cube.rotate_right_clockwise()
            print("Правая грань повернута по часовой стрелке")
        elif choice == 5:
            cube.rotate_right_counter_clockwise()
            print("Правая грань повернута против часовой стрелки")
        elif choice == 6:
            cube.rotate_left_clockwise()
            print("Левая грань повернута по часовой стрелке")
        elif choice == 7:
            cube.rotate_left_counter_clockwise()
            print("Левая грань повернута против часовой стрелки")
        elif choice == 8:
            cube.rotate_up_clockwise()
            print("Верхняя грань повернута по часовой стрелке")
        elif choice == 9:
            cube.rotate_up_counter_clockwise()
            print("Верхняя грань повернута против часовой стрелки")
        elif choice == 10:
            cube.rotate_down_clockwise()
            print("Нижняя грань повернута по часовой стрелке")
        elif choice == 11:
            cube.rotate_down_counter_clockwise()
            print("Нижняя грань повернута против часовой стрелки")
        elif choice == 12:
            cube.rotate_back_clockwise()
            print("Задняя грань повернута по часовой стрелке")
        elif choice == 13:
            cube.rotate_back_counter_clockwise()
            print("Задняя грань повернута против часовой стрелки")
        elif choice == 14:
            moves = input("Сколько перемешиваний? (по умолчанию 20): ")
            moves = int(moves) if moves.isdigit() else 20
            cube.scramble(moves)
            print(f"Кубик перемешан ({moves} движений)")
        elif choice == 15:
            if cube.is_solved():
                print("Кубик решен! 🎉")
            else:
                print("Кубик не решен")
        elif choice == 16:
            cube.initialize()
            print("Кубик возвращен в начальное состояние")
        else:
            print("Неверная опция!")


if __name__ == "__main__":
    main()