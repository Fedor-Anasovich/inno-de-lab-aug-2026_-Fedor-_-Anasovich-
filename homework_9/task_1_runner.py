# task_1_runner.py
from models.trainee_models import Trainee

if __name__ == "__main__":
    print("=== ЗАПУСК: ТЕСТИРОВАНИЕ БАЗОВОГО КЛАССА СТАЖЕРА ===")

    trainee = Trainee(name="Иван", surname="Иванов", score=9, passing_grade=10)

    trainee.do_homework()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    trainee.miss_lecture()
    print(f"Баллы: {trainee.score}, Прошел курс: {trainee.is_passing()}")

    try:
        trainee.score = -5
    except ValueError as e:
        print(f"Ожидаемая ошибка валидации: {e}")
