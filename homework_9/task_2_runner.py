# task_2_runner.py
from models.trainee_models import Trainee, HardworkingTrainee, AuditTrainee, Cohort

if __name__ == "__main__":
    print("=== ЗАПУСК: ДЕМОНСТРАЦИЯ ООП И РАБОТЫ С ГРУППОЙ ===")

    std_trainee = Trainee("Алексей", "Смирнов", score=8, passing_grade=10)
    hard_trainee = HardworkingTrainee("Елена", "Петрова", score=8, passing_grade=10)
    audit_trainee = AuditTrainee("Дмитрий", "Сидоров", score=0, passing_grade=10)

    cohort = Cohort("Python Advanced")
    cohort.add_trainee(std_trainee)
    cohort.add_trainee(hard_trainee)
    cohort.add_trainee(audit_trainee)

    cohort.conduct_lecture()
    hard_trainee.do_homework()

    print(f"\n=== УСПЕВАЕМОСТЬ ГРУППЫ '{cohort.title}' ===")
    for student in cohort.trainees:
        print(f"{student.name} {student.surname} | Баллы: {student.score} | Проходит: {student.is_passing()}")

    print("\nУспешно зачислены на следующий модуль:")
    for student in cohort.get_passing_students():
        print(f"- {student.name} {student.surname}")
