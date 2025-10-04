from models import PostMachine, ProgramLibrary


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