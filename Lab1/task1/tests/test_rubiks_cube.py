import pytest
import sys
import os

# Добавляем путь к корню проекта в Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.RubiksCube import RubiksCube
from models.Color import Color


# Фикстуры для тестов
@pytest.fixture
def solved_cube():
    """Возвращает собранный кубик"""
    return RubiksCube()

@pytest.fixture
def scrambled_cube():
    """Возвращает перемешанный кубик"""
    cube = RubiksCube()
    cube.scramble(10)
    return cube

class TestRubiksCubeInitialization:
    """Тесты инициализации кубика"""

    def test_initial_state(self, solved_cube):
        """Тест начального состояния кубика"""
        # Проверяем что все грани правильного цвета
        assert solved_cube.is_face_uniform(solved_cube.front)
        assert solved_cube.is_face_uniform(solved_cube.back)
        assert solved_cube.is_face_uniform(solved_cube.left)
        assert solved_cube.is_face_uniform(solved_cube.right)
        assert solved_cube.is_face_uniform(solved_cube.up)
        assert solved_cube.is_face_uniform(solved_cube.down)

        # Проверяем конкретные цвета
        assert solved_cube.front[0][0] == Color.RED
        assert solved_cube.back[0][0] == Color.ORANGE
        assert solved_cube.left[0][0] == Color.GREEN
        assert solved_cube.right[0][0] == Color.BLUE
        assert solved_cube.up[0][0] == Color.WHITE
        assert solved_cube.down[0][0] == Color.YELLOW

    def test_initialize_reset(self, scrambled_cube):
        """Тест сброса кубика в начальное состояние"""
        # Перемешиваем и сбрасываем
        scrambled_cube.initialize()

        # Проверяем что кубик снова собран
        assert scrambled_cube.is_solved()
        assert scrambled_cube.front[1][1] == Color.RED
        assert scrambled_cube.up[1][1] == Color.WHITE


class TestFaceRotations:
    """Тесты поворотов отдельных граней"""

    def test_rotate_face_clockwise_formula(self, solved_cube):
        """Тест формулы поворота по часовой (твой алгоритм)"""
        # Создаем грань с существующими цветами
        test_face = [
            [Color.RED, Color.GREEN, Color.BLUE],
            [Color.WHITE, Color.YELLOW, Color.ORANGE],
            [Color.NONE, Color.WHITE, Color.RED]  # Только существующие цвета!
        ]

        solved_cube.rotate_face_clockwise(test_face)

        assert test_face[0][0] == Color.NONE
        assert test_face[0][1] == Color.WHITE
        assert test_face[0][2] == Color.RED

        assert test_face[1][0] == Color.WHITE
        assert test_face[1][1] == Color.YELLOW
        assert test_face[1][2] == Color.GREEN

    def test_rotate_face_counter_clockwise_formula(self, solved_cube):
        """Тест формулы поворота против часовой (твой алгоритм)"""
        test_face = [
            [Color.RED, Color.GREEN, Color.BLUE],
            [Color.WHITE, Color.YELLOW, Color.ORANGE],
            [Color.NONE, Color.WHITE, Color.RED]
        ]

        solved_cube.rotate_face_counter_clockwise(test_face)

        assert test_face[0][0] == Color.BLUE
        assert test_face[0][1] == Color.ORANGE
        assert test_face[0][2] == Color.RED

        assert test_face[1][0] == Color.GREEN
        assert test_face[1][1] == Color.YELLOW
        assert test_face[1][2] == Color.WHITE

    def test_rotate_face_identity_clockwise(self, solved_cube):
        """Тест что 4 поворота по часовой возвращают к исходному"""
        test_face = [
            [Color.RED, Color.GREEN, Color.BLUE],
            [Color.WHITE, Color.YELLOW, Color.ORANGE],
            [Color.NONE, Color.WHITE, Color.RED]
        ]
        original = [row[:] for row in test_face]

        # 4 поворота по часовой = исходное состояние
        for _ in range(4):
            solved_cube.rotate_face_clockwise(test_face)
        assert test_face == original

    def test_rotate_face_identity_counter_clockwise(self, solved_cube):
        """Тест что 4 поворота против часовой возвращают к исходному"""
        test_face = [
            [Color.RED, Color.GREEN, Color.BLUE],
            [Color.WHITE, Color.YELLOW, Color.ORANGE],
            [Color.NONE, Color.WHITE, Color.RED]
        ]
        original = [row[:] for row in test_face]

        # 4 поворота против часовой = исходное состояние
        for _ in range(4):
            solved_cube.rotate_face_counter_clockwise(test_face)
        assert test_face == original

    def test_clockwise_and_counter_clockwise_cancel(self, solved_cube):
        """Тест что поворот по и против часовой компенсируют друг друга"""
        test_face = [
            [Color.RED, Color.GREEN, Color.BLUE],
            [Color.WHITE, Color.YELLOW, Color.ORANGE],
            [Color.NONE, Color.WHITE, Color.RED]
        ]
        original = [row[:] for row in test_face]

        solved_cube.rotate_face_clockwise(test_face)
        solved_cube.rotate_face_counter_clockwise(test_face)

        assert test_face == original


class TestCubeRotations:
    """Тесты поворотов всего кубика"""

    def test_rotate_front_clockwise(self, solved_cube):
        """Тест поворота передней грани по часовой стрелке"""
        original_up = [row[:] for row in solved_cube.up]

        solved_cube.rotate_front_clockwise()

        # Проверяем что что-то изменилось
        assert solved_cube.up[2] != original_up[2]
        # 4 поворота должны вернуть к исходному состоянию
        for _ in range(3):
            solved_cube.rotate_front_clockwise()
        assert solved_cube.is_solved()

    def test_rotate_front_counter_clockwise(self, solved_cube):
        """Тест поворота передней грани против часовой стрелки"""
        solved_cube.rotate_front_counter_clockwise()
        solved_cube.rotate_front_clockwise()

        # Против + по часовой = исходное состояние
        assert solved_cube.is_solved()

    def test_rotate_right_clockwise(self, solved_cube):
        """Тест поворота правой грани"""
        solved_cube.rotate_right_clockwise()
        solved_cube.rotate_right_counter_clockwise()

        assert solved_cube.is_solved()

    def test_rotate_left_clockwise(self, solved_cube):
        """Тест поворота левой грани"""
        solved_cube.rotate_left_clockwise()
        solved_cube.rotate_left_counter_clockwise()

        assert solved_cube.is_solved()

    def test_rotate_up_clockwise(self, solved_cube):
        """Тест поворота верхней грани"""
        solved_cube.rotate_up_clockwise()
        solved_cube.rotate_up_counter_clockwise()

        assert solved_cube.is_solved()

    def test_rotate_down_clockwise(self, solved_cube):
        """Тест поворота нижней грани"""
        solved_cube.rotate_down_clockwise()
        solved_cube.rotate_down_counter_clockwise()

        assert solved_cube.is_solved()

    def test_rotate_back_clockwise(self, solved_cube):
        """Тест поворота задней грани"""
        solved_cube.rotate_back_clockwise()
        solved_cube.rotate_back_counter_clockwise()

        assert solved_cube.is_solved()

class TestScrambling:
    """Тесты перемешивания кубика"""

    def test_scramble_changes_cube(self, solved_cube):
        """Тест что перемешивание изменяет кубик"""
        original_state = self._get_cube_state(solved_cube)

        solved_cube.scramble(5)
        new_state = self._get_cube_state(solved_cube)

        assert original_state != new_state

    def test_scramble_with_custom_moves(self, solved_cube):
        """Тест перемешивания с заданным количеством ходов"""
        solved_cube.scramble(15)
        # Просто проверяем что не упало с ошибкой
        assert True

    def _get_cube_state(self, cube):
        """Вспомогательный метод для получения состояния кубика"""
        return str(cube.front) + str(cube.back) + str(cube.left) + str(cube.right) + str(cube.up) + str(cube.down)


def test_main_function_options(monkeypatch, capsys):
    """Тест различных опций главного меню"""
    inputs = ['1', '15', '16', '0']  # Показать -> Проверить -> Сбросить -> Выйти
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # ЗАМЕНИ СТРОКУ НИЖЕ:
    from main import main

    # Тестируем что функция не падает с ошибками
    try:
        main()
    except SystemExit:
        pass  # Ожидаемый выход из программы

    captured = capsys.readouterr()
    # Проверяем что меню отображалось
    assert "КУБИК РУБИКА" in captured.out




