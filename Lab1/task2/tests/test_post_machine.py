import pytest
import builtins
import sys
import os

# Добавляем путь к корню проекта в Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.post_machine import PostMachine
from models.program_library import ProgramLibrary
from main import PostMachineUI, PostMachineDemo


# Фикстуры для тестов
@pytest.fixture
def empty_machine():
    """Пустая машина"""
    return PostMachine(5)


@pytest.fixture
def machine_with_program():
    """Машина с загруженной программой"""
    machine = PostMachine(5)
    machine.load_program(["V", "->", "V", "!"])
    return machine


@pytest.fixture
def running_machine():
    """Запущенная машина"""
    machine = PostMachine(5)
    machine.load_program(["V", "->", "V", "!"])
    machine._is_running = True
    return machine


class TestPostMachineGettersAndSetters:
    """Тесты геттеров и сеттеров"""

    def test_get_tape_returns_copy(self, machine_with_program):
        """Тест что get_tape возвращает копию"""
        tape = machine_with_program.get_tape()
        tape[0] = 999  # Пытаемся изменить

        # Оригинал не должен измениться
        assert machine_with_program.get_tape()[0] == 0

    def test_set_tape_valid(self, empty_machine):
        """Тест установки корректной ленты"""
        new_tape = [1, 0, 1, 0, 1]
        empty_machine.set_tape(new_tape)

        assert empty_machine.get_tape() == [1, 0, 1, 0, 1]
        # Проверяем что сохраняется копия
        new_tape[0] = 0
        assert empty_machine.get_tape()[0] == 1

    def test_set_tape_invalid(self, empty_machine):
        """Тест установки некорректной ленты"""
        with pytest.raises(ValueError, match="Лента должна быть списком из 0 и 1"):
            empty_machine.set_tape([1, 2, 3])  # Некорректные значения

        with pytest.raises(ValueError):
            empty_machine.set_tape("not a list")  # Не список

    def test_set_tape_adjusts_position(self, empty_machine):
        """Тест что позиция корректируется при установке короткой ленты"""
        empty_machine.set_position(4)  # Последняя позиция
        empty_machine.set_tape([1, 0])  # Более короткая лента

        assert empty_machine.get_position() == 1  # Должна скорректироваться

    def test_set_position_valid(self, empty_machine):
        """Тест установки корректной позиции"""
        empty_machine.set_position(3)
        assert empty_machine.get_position() == 3

    def test_set_position_invalid(self, empty_machine):
        """Тест установки некорректной позиции"""
        with pytest.raises(ValueError, match="Позиция должна быть в пределах ленты"):
            empty_machine.set_position(10)  # За пределами

        with pytest.raises(ValueError):
            empty_machine.set_position(-1)  # Отрицательная


class TestPostMachineCommands:
    """Тесты выполнения команд"""

    def test_command_V(self, empty_machine):
        """Тест команды V (поставить метку)"""
        empty_machine._execute_command("V")
        assert empty_machine.get_tape()[0] == 1
        assert empty_machine.get_current_command() == 1

    def test_command_X(self, empty_machine):
        """Тест команды X (стереть метку)"""
        empty_machine._tape[0] = 1  # Сначала ставим метку
        empty_machine._execute_command("X")
        assert empty_machine.get_tape()[0] == 0
        assert empty_machine.get_current_command() == 1

    def test_command_arrow_right(self, empty_machine):
        """Тест команды -> (движение вправо)"""
        empty_machine._execute_command("->")
        assert empty_machine.get_position() == 1
        assert empty_machine.get_current_command() == 1

    def test_command_arrow_right_expansion(self):
        """Тест что лента расширяется при движении вправо"""
        machine = PostMachine(3)
        machine.set_position(2)  # Последняя позиция
        machine._execute_command("->")  # Двигаемся за пределы

        assert machine.get_position() == 3
        assert len(machine.get_tape()) == 4  # Лента расширилась
        assert machine.get_tape()[3] == 0  # Новая ячейка пустая

    def test_command_arrow_left(self, empty_machine):
        """Тест команды <- (движение влево)"""
        empty_machine.set_position(2)
        empty_machine._execute_command("<-")
        assert empty_machine.get_position() == 1
        assert empty_machine.get_current_command() == 1

    def test_command_arrow_left_at_zero(self, empty_machine):
        """Тест команды <- на нулевой позиции"""
        empty_machine._execute_command("<-")  # Пытаемся уйти в минус
        assert empty_machine.get_position() == 0  # Остается на 0
        assert empty_machine.get_current_command() == 1

    def test_command_stop(self, running_machine):
        """Тест команды ! (остановка)"""
        running_machine._execute_command("!")
        assert not running_machine.get_is_running()

    def test_unknown_command(self, empty_machine):
        """Тест неизвестной команды"""
        initial_command = empty_machine.get_current_command()
        empty_machine._execute_command("UNKNOWN")
        # Должен просто перейти к следующей команде
        assert empty_machine.get_current_command() == initial_command + 1


class TestInputFromConsole:
    """Тесты ввода с консоли"""

    def test_input_from_console_valid(self, monkeypatch, capsys):
        """Тест корректного ввода с консоли"""
        machine = PostMachine()

        # Имитируем ввод
        inputs = ["5", "3", "V", "->", "!"]
        input_iterator = iter(inputs)
        monkeypatch.setattr(builtins, 'input', lambda _: next(input_iterator))

        machine.input_from_console()

        captured = capsys.readouterr()
        assert "Машина успешно настроена!" in captured.out
        assert len(machine.get_tape()) == 5
        assert machine.get_program() == ["V", "->", "!"]

    def test_input_from_console_invalid(self, monkeypatch, capsys):
        """Тест некорректного ввода с консоли"""
        machine = PostMachine()

        monkeypatch.setattr(builtins, 'input', lambda _: "invalid")

        machine.input_from_console()

        captured = capsys.readouterr()
        assert "Ошибка ввода данных!" in captured.out


class TestUICoverage:
    """Тесты для покрытия UI методов"""

    def test_load_program_menu_valid_choice(self, monkeypatch, capsys):
        """Тест загрузки программы через меню"""
        ui = PostMachineUI()
        monkeypatch.setattr(builtins, 'input', lambda _: "1")  # Выбираем простую программу

        ui.load_program_menu()

        captured = capsys.readouterr()
        assert "Загружена Простая программа" in captured.out
        assert ui.machine.get_program() == ["V", "->", "V", "!"]

    def test_load_custom_program_valid(self, monkeypatch, capsys):
        """Тест загрузки кастомной программы"""
        ui = PostMachineUI()

        # Исправленный monkeypatch - input без аргумента
        monkeypatch.setattr(builtins, 'input', lambda: "V,->,X,!")

        ui.load_custom_program()

        captured = capsys.readouterr()
        assert "Программа загружена" in captured.out
        assert ui.machine.get_program() == ["V", "->", "X", "!"]

    def test_execute_step_no_program(self, capsys):
        """Тест выполнения шага без программы"""
        ui = PostMachineUI()

        ui.execute_step()

        captured = capsys.readouterr()
        assert "Сначала загрузите программу!" in captured.out

    def test_run_program_no_program(self, capsys):
        """Тест запуска программы без программы"""
        ui = PostMachineUI()

        ui.run_program()

        captured = capsys.readouterr()
        assert "Сначала загрузите программу!" in captured.out

    def test_display_state(self, capsys):
        """Тест отображения состояния"""
        ui = PostMachineUI()
        ui.machine.load_program(["V", "!"])

        ui.display_state()

        captured = capsys.readouterr()
        assert "Состояние машины" in captured.out
        assert "Программа:" in captured.out

    def test_compare_machines(self, capsys):
        """Тест сравнения машин"""
        ui = PostMachineUI()
        ui.machine.load_program(["V", "!"])

        ui.compare_machines()

        captured = capsys.readouterr()
        assert "Сравнение машин" in captured.out
        assert "Машины идентичны" in captured.out

    def test_test_operators(self, capsys):
        """Тест операторов сравнения"""
        ui = PostMachineUI()

        ui.test_operators()

        captured = capsys.readouterr()
        assert "Тестирование операторов" in captured.out


class TestDemoCoverage:
    """Тесты демонстрационных методов"""

    def test_demonstrate_simple_program(self, capsys):
        """Тест демонстрации простой программы"""
        PostMachineDemo.demonstrate_simple_program()

        captured = capsys.readouterr()
        assert "ДЕМОНСТРАЦИЯ: Простая программа" in captured.out
        assert "Программа: V, ->, V, !" in captured.out

    def test_demonstrate_conditional_program(self, capsys):
        """Тест демонстрации программы с условием"""
        PostMachineDemo.demonstrate_conditional_program()

        captured = capsys.readouterr()
        assert "ДЕМОНСТРАЦИЯ: Программа с условием" in captured.out


if __name__ == "__main__":
    pytest.main([__file__, "-v"])