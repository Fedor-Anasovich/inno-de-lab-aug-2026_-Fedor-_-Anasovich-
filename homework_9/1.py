class Trainee:
    # Аннотации типов для атрибутов класса
    name: str
    surname: str
    passing_grade: int
    __score: int

    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10) -> None:
        self.name = name
        self.surname = surname
        self.passing_grade = passing_grade
        # Инициализируем через сеттер для автоматической проверки начального значения score
        self.score = score

    @property
    def score(self) -> int:
        """Возвращает текущее количество баллов стажера."""
        return self.__score

    @score.setter
    def score(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError(f"Expected value of type int, got {type(value)}")
        if value < 0:
            raise ValueError("The score shouldn't be less than 0!")
        self.__score = value

    def do_homework(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_homework(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def visit_lecture(self) -> None:
        """Increases score by 1"""
        self.score += 1

    def miss_lecture(self) -> None:
        """Decreases score by 1"""
        self.score -= 1

    def is_passing(self) -> bool:
        """Проверяет, набрал ли стажер проходной балл."""
        return self.score >= self.passing_grade


# Тестирование программы
if __name__ == "__main__":
    print("=== ПРОВЕРКА УСПЕВАЕМОСТИ СТАЖЕРА ===")

    # Создание стажера с начальным баллом 9 и проходным баллом 10
    trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

    # Выполнение домашнего задания и проверка статуса
    trainee.do_homework()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # Пропуск лекции и проверка статуса
    trainee.miss_lecture()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    # Проверка валидации (попытка задать отрицательное значение)
    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Ошибка: {e}")