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