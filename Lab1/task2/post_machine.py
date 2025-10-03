class PostMachine:
    """ Класс, реализующий машину Поста с полной инкапсуляцией """
    def __init__(self, tape_size=20):
        self._tape = [0] * tape_size # лента основной памяти машины
        self._position = 0 # указатель на текущую позицию
        self._program = [] # пустой список команд
        self._current_command = 0 # счетчик программ
        self._is_running = False # Флаг выполнения программы

    def __copy__(self): # поверхностное копирование
        new_machine = PostMachine(len(self._tape))
        new_machine._tape = self._tape.copy()
        new_machine._position = self._position
        new_machine._program = self._program.copy()
        new_machine._current_command = self._current_command
        new_machine._is_running = self._is_running
        return new_machine

    def __deepcopy__(self, memo):
        return self.__copy__()

    def __eq__(self, other): # проверка на одинаковые машины Поста (сравнивает их содержание)
        if not isinstance(other, PostMachine):
            return False
        return (self._tape == other._tape and
                self._position == other._position and
                self._program == other._program and
                self._current_command == other._current_command and
                self._is_running == other._is_running)

    def __ne__(self, other): # Просто инвертирует результат сравнения на равенство
        return not self.__eq__(other)

    def __str__(self):
        tape_display = " ".join(f"[{cell}]" if i == self._position else f" {cell} "
                                for i, cell in enumerate(self._tape))
        return f"PostMachine(позиция={self._position}, команда={self._current_command}, работает={self._is_running})\nЛента: {tape_display}"

    def input_from_console(self): # ввод параметров для машины от пользователя
        try:
            size = int(input("Введите размер ленты: "))
            self._tape = [0] * size
            self._position = 0

            count = int(input("Введите количество команд: "))
            self._program = []
            print("Введите команды (V, X, ->, <-, ?n,m, !):")
            for i in range(count):
                cmd = input(f"Команда {i}: ").strip()
                self._program.append(cmd)

            self._current_command = 0
            self._is_running = False
            print("Машина успешно настроена!")
        except ValueError: # ловит ошибки
            print("Ошибка ввода данных!")

    # гетеры
    def get_tape(self): # чтобы нельзя было изменять оригинал
        return self._tape.copy()

    def get_position(self):
        return self._position # возвращает текущую позицию

    def get_program(self):
        return self._program.copy() # копию программы

    def get_current_command(self):
        return self._current_command # Текущий номер команды

    def get_is_running(self):
        return self._is_running # Статус выполнения

    def set_tape(self, new_tape):
        if isinstance(new_tape, list) and all(cell in (0, 1) for cell in new_tape): # проверка типа данных
            self._tape = new_tape.copy() # сохраняем копию
            if self._position >= len(self._tape):
                self._position = len(self._tape) - 1
        else:
            raise ValueError("Лента должна быть списком из 0 и 1")

    def set_position(self, new_position):
        if 0 <= new_position < len(self._tape):
            self._position = new_position
        else:
            raise ValueError("Позиция должна быть в пределах ленты")

    def reset(self): # переводит машину в начальное состояние, сохраняя размер ленты
        self._tape = [0] * len(self._tape)
        self._position = 0
        self._current_command = 0
        self._is_running = False

    def load_program(self, commands):
        if not isinstance(commands, list):
            raise ValueError("Программа должна быть списком команд")
        self._program = commands.copy()
        self.reset()
        self._is_running = True

    def step(self):
        if not self._is_running and self._current_command < len(self._program):
            self._is_running = True # Если машина остановлена, но есть команды для выполнения - запускает ее

        if not self._is_running or self._current_command >= len(self._program):
            return False # когда шаг не выполняется

        command = self._program[self._current_command] # берет из программы команду и выполняет ее
        self._execute_command(command)

        return self._is_running and self._current_command < len(self._program)

    def run(self): # запускат машину и выполняет все программы
        self._is_running = True
        steps = 0
        while self.step():
            steps += 1
            if steps > 1000:
                print("Превышено максимальное количество шагов!")
                break
        return steps

    def _execute_command(self, command): # символы и действия
        if command == "V":
            self._tape[self._position] = 1
            self._current_command += 1

        elif command == "X":
            self._tape[self._position] = 0
            self._current_command += 1

        elif command == "->":
            self._position += 1
            if self._position >= len(self._tape):
                self._tape.append(0)
            self._current_command += 1

        elif command == "<-":
            self._position -= 1
            if self._position < 0:
                self._position = 0
            self._current_command += 1

        elif command.startswith("?"): # условный переход
            self._handle_conditional_jump(command)

        elif command == "!":
            self._is_running = False

        else:
            self._current_command += 1

    def _handle_conditional_jump(self, command): # обработка метода условного перехода
        params = command[1:].split(",")
        if len(params) == 2:
            cmd_if_true = int(params[0])
            cmd_if_false = int(params[1])

            if cmd_if_true >= len(self._program) or cmd_if_false >= len(self._program):
                raise ValueError(f"Переход за пределы программы: {command}")

            if self._tape[self._position] == 1:
                self._current_command = cmd_if_true
            else:
                self._current_command = cmd_if_false

    def display_tape(self): # проработка вывода
        tape_str = ""
        for i, cell in enumerate(self._tape):
            if i == self._position:
                tape_str += f"[{cell}]"
            else:
                tape_str += f" {cell} "
        return tape_str

    def display_state(self): # проработка вывода
        return (f"Текущая команда: {self._current_command}\n"
                f"Состояние: {'работает' if self._is_running else 'остановлена'}\n"
                f"Лента: {self.display_tape()}")


class ProgramLibrary:
    """Библиотека готовых программ для машины Поста"""

    @staticmethod
    def get_simple_program():
        return ["V", "->", "V", "!"]

    @staticmethod
    def get_conditional_program():
        return ["?1,3", "X", "!", "V", "!"]

    @staticmethod
    def get_infinite_movement():
        return ["V", "->", "V", "->", "?0,0"]

    @staticmethod
    def get_tape_cleaner():
        return ["?1,2", "X", "->", "?1,0", "!"]

    @staticmethod
    def get_alternating_marks():
        return ["V", "->", "X", "->", "V", "->", "X", "!"]


class PostMachineUI:
    """Пользовательский интерфейс для работы с машиной Поста"""

    def __init__(self):
        self.machine = PostMachine()
        self.library = ProgramLibrary()

    def display_menu(self):
        print("\n" + "=" * 50)
        print("           МАШИНА ПОСТА")
        print("=" * 50)
        print("1. Создать новую машину")
        print("2. Загрузить программу")
        print("3. Выполнить шаг")
        print("4. Запустить программу")
        print("5. Показать состояние")
        print("6. Сравнить с другой машиной")
        print("7. Тестирование операторов")
        print("8. Выход")
        print("-" * 50)

    def create_new_machine(self):
        try:
            size = int(input("Введите размер ленты: "))
            self.machine = PostMachine(size)
            print(f"Создана новая машина с лентой размером {size}")
        except ValueError:
            print("Ошибка: введите целое число")

    def load_program_menu(self):
        print("\n--- Загрузка программы ---")
        print("1. Простая программа (две метки)")
        print("2. Программа с условием")
        print("3. Бесконечное движение")
        print("4. Очиститель ленты")
        print("5. Чередующиеся метки")
        print("6. Ввести свою программу")
        print("7. Ввести с консоли")

        choice = input("Выберите опцию: ")

        programs = {
            "1": ("Простая программа", self.library.get_simple_program()),
            "2": ("Программа с условием", self.library.get_conditional_program()),
            "3": ("Бесконечное движение", self.library.get_infinite_movement()),
            "4": ("Очиститель ленты", self.library.get_tape_cleaner()),
            "5": ("Чередующиеся метки", self.library.get_alternating_marks())
        }

        if choice in programs:
            name, program = programs[choice]
            self.machine.load_program(program)
            print(f"Загружена {name}")

        elif choice == "6":
            self.load_custom_program()

        elif choice == "7":
            self.machine.input_from_console()

        else:
            print("Неверный выбор")

    def load_custom_program(self):
        print("Введите команды через запятую (V, X, ->, <-, ?n,m, !):")
        commands_input = input().strip()
        commands = [cmd.strip() for cmd in commands_input.split(",")]

        try:
            self.machine.load_program(commands)
            print(f"Программа загружена: {commands}")
        except Exception as e:
            print(f"Ошибка загрузки программы: {e}")

    def execute_step(self):
        if not self.machine.get_program():
            print("Сначала загрузите программу!")
            return

        if not self.machine.get_is_running():
            self.machine._is_running = True

        print("\nДо шага:")
        print(self.machine.display_state())

        if self.machine.step():
            print("\nПосле шага:")
            print(self.machine.display_state())
        else:
            print("Программа завершена!")

    def run_program(self):
        if not self.machine.get_program():
            print("Сначала загрузите программу!")
            return

        print("Запуск программы...")
        print("Начальное состояние:")
        print(self.machine.display_state())

        steps = self.machine.run()

        print(f"\nВыполнено шагов: {steps}")
        print("Конечное состояние:")
        print(self.machine.display_state())

    def display_state(self):
        print("\n--- Состояние машины ---")
        print(self.machine.display_state())
        print(f"Программа: {self.machine.get_program()}")

    def compare_machines(self):
        print("\n--- Сравнение машин ---")

        machine_copy = self.machine.__copy__()

        print("Текущая машина:")
        print(self.machine)

        print("\nКопия машины:")
        print(machine_copy)

        if self.machine == machine_copy:
            print("\n✓ Машины идентичны")
        else:
            print("\n✗ Машины различны")

        if machine_copy.get_position() + 1 < len(machine_copy.get_tape()):
            machine_copy.set_position(machine_copy.get_position() + 1)
            print(f"\nПосле модификации копии:")

            if self.machine != machine_copy:
                print("✗ Машины теперь различны")

    def test_operators(self):
        print("\n--- Тестирование операторов ---")

        machine1 = PostMachine(5)
        machine1.load_program(["V", "->", "!"])
        machine2 = machine1.__copy__()

        print("Машина 1:", machine1)
        print("Машина 2:", machine2)
        print("machine1 == machine2:", machine1 == machine2)

        machine3 = machine1.__deepcopy__({})
        print("machine1 == machine3:", machine1 == machine3)

        machine2.set_position(1)
        print("После изменения machine2:")
        print("machine1 == machine2:", machine1 == machine2)
        print("machine1 != machine2:", machine1 != machine2)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Выберите опцию: ").strip()

            try:
                if choice == "1":
                    self.create_new_machine()
                elif choice == "2":
                    self.load_program_menu()
                elif choice == "3":
                    self.execute_step()
                elif choice == "4":
                    self.run_program()
                elif choice == "5":
                    self.display_state()
                elif choice == "6":
                    self.compare_machines()
                elif choice == "7":
                    self.test_operators()
                elif choice == "8":
                    print("Выход из программы...")
                    break
                else:
                    print("Неверный выбор, попробуйте снова")
            except Exception as e:
                print(f"Произошла ошибка: {e}")


class PostMachineDemo:
    """Демонстрационный класс с примерами работы машины Поста"""

    @staticmethod
    def demonstrate_simple_program():
        print("\n" + "=" * 60)
        print("ДЕМОНСТРАЦИЯ: Простая программа")
        print("=" * 60)

        machine = PostMachine(5)
        program = ProgramLibrary.get_simple_program()
        machine.load_program(program)

        print("Программа: V, ->, V, !")
        print("Начальное состояние:")
        print(machine.display_state())

        machine.run()

        print("Конечное состояние:")
        print(machine.display_state())
        print("Результат: Две метки на ленте")

    @staticmethod
    def demonstrate_conditional_program():
        print("\n" + "=" * 60)
        print("ДЕМОНСТРАЦИЯ: Программа с условием")
        print("=" * 60)

        machine = PostMachine(5)
        program = ProgramLibrary.get_conditional_program()
        machine.load_program(program)

        print("Программа: ?1,3, X, !, V, !")
        print("Начальное состояние (пустая ячейка):")
        print(machine.display_state())

        machine.run()

        print("После выполнения (должна появиться метка):")
        print(machine.display_state())

        # Запускаем еще раз
        machine.reset()
        machine.set_tape([1, 0, 0, 0, 0])  # Ставим метку в начало
        machine.run()

        print("После выполнения с начальной меткой (метка должна исчезнуть):")
        print(machine.display_state())

    @staticmethod
    def run_all_demos():
        PostMachineDemo.demonstrate_simple_program()
        PostMachineDemo.demonstrate_conditional_program()


def main():
    print("ДЕМОНСТРАЦИЯ МАШИНЫ ПОСТА")

    # Запуск демонстраций
    demo_choice = input("\nЗапустить демонстрации? (y/n): ").lower()
    if demo_choice == 'y':
        PostMachineDemo.run_all_demos()

    # Запуск интерактивного режима
    ui = PostMachineUI()
    ui.run()


if __name__ == "__main__":
    main()