# models/trainee_models.py

class Trainee:
    name: str
    surname: str
    passing_grade: int
    __score: int

    def __init__(self, name: str, surname: str, score: int = 0, passing_grade: int = 10) -> None:
        self.name = name
        self.surname = surname
        self.passing_grade = passing_grade
        self.score = score

    @property
    def score(self) -> int:
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
        return self.score >= self.passing_grade


class HardworkingTrainee(Trainee):
    """Класс для стажеров-трудоголиков."""
    def do_homework(self) -> None:
        """Increases score by 2"""
        self.score += 2


class AuditTrainee(Trainee):
    """Класс для вольнослушателей."""
    def is_passing(self) -> bool:
        return True


class Cohort:
    title: str
    trainees: list[Trainee]

    def __init__(self, title: str) -> None:
        self.title = title
        self.trainees = []

    def add_trainee(self, trainee: Trainee) -> None:
        self.trainees.append(trainee)

    def conduct_lecture(self) -> None:
        for trainee in self.trainees:
            trainee.visit_lecture()

    def get_passing_students(self) -> list[Trainee]:
        return [trainee for trainee in self.trainees if trainee.is_passing()]
