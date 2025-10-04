class PostMachine:
    """ Класс, реализующий машину Поста с полной инкапсуляцией """

    def __init__(self, tape_size=20):
        self._tape = [0] * tape_size
        self._position = 0
        self._program = []
        self._current_command = 0
        self._is_running = False

    def __copy__(self):
        new_machine = PostMachine(len(self._tape))
        new_machine._tape = self._tape.copy()
        new_machine._position = self._position
        new_machine._program = self._program.copy()
        new_machine._current_command = self._current_command
        new_machine._is_running = self._is_running
        return new_machine

    def __deepcopy__(self, memo):
        return self.__copy__()

    def __eq__(self, other):
        if not isinstance(other, PostMachine):
            return False
        return (self._tape == other._tape and
                self._position == other._position and
                self._program == other._program and
                self._current_command == other._current_command and
                self._is_running == other._is_running)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        tape_display = " ".join(f"[{cell}]" if i == self._position else f" {cell} "
                                for i, cell in enumerate(self._tape))
        return f"PostMachine(позиция={self._position}, команда={self._current_command}, работает={self._is_running})\nЛента: {tape_display}"

    def input_from_console(self):
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
        except ValueError:
            print("Ошибка ввода данных!")

    # Геттеры
    def get_tape(self):
        return self._tape.copy()

    def get_position(self):
        return self._position

    def get_program(self):
        return self._program.copy()

    def get_current_command(self):
        return self._current_command

    def get_is_running(self):
        return self._is_running

    # Сеттеры
    def set_tape(self, new_tape):
        if isinstance(new_tape, list) and all(cell in (0, 1) for cell in new_tape):
            self._tape = new_tape.copy()
            if self._position >= len(self._tape):
                self._position = len(self._tape) - 1
        else:
            raise ValueError("Лента должна быть списком из 0 и 1")

    def set_position(self, new_position):
        if 0 <= new_position < len(self._tape):
            self._position = new_position
        else:
            raise ValueError("Позиция должна быть в пределах ленты")

    def reset(self):
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
            self._is_running = True

        if not self._is_running or self._current_command >= len(self._program):
            return False

        command = self._program[self._current_command]
        self._execute_command(command)

        return self._is_running and self._current_command < len(self._program)

    def run(self):
        self._is_running = True
        steps = 0
        while self.step():
            steps += 1
            if steps > 1000:
                print("Превышено максимальное количество шагов!")
                break
        return steps

    def _execute_command(self, command):
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

        elif command.startswith("?"):
            self._handle_conditional_jump(command)

        elif command == "!":
            self._is_running = False

        else:
            self._current_command += 1

    def _handle_conditional_jump(self, command):
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

    def display_tape(self):
        tape_str = ""
        for i, cell in enumerate(self._tape):
            if i == self._position:
                tape_str += f"[{cell}]"
            else:
                tape_str += f" {cell} "
        return tape_str

    def display_state(self):
        return (f"Текущая команда: {self._current_command}\n"
                f"Состояние: {'работает' if self._is_running else 'остановлена'}\n"
                f"Лента: {self.display_tape()}")