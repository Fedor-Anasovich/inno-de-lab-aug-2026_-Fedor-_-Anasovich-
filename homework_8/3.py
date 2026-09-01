import functools
from typing import Any

# Константа на уровне модуля
DEFAULT_RETURN_INDEX_BASE = 10.0


# Реализация функции с безопасной обработкой исключений и аннотациями по ТЗ
def calculate_overdue_fine(
        days_overdue: Any, fine_rate: float, title: str
) -> tuple[float, float] | None:
    """Рассчитывает сумму штрафа и technical индекс оборачиваемости фильма.

    Функция устойчива к некорректным входным данным и обрабатывает следующие
    ошибки:
        - TypeError: возникает при передаче сложных структур (например, списков)
          вместо чисел или строк.
        - ValueError: возникает при невозможности преобразовать строку в число.
        - ZeroDivisionError: возникает, если количество дней просрочки равно 0.

    Args:
        days_overdue (Any): Количество дней просрочки (может быть любого типа
            из-за сырых данных).
        fine_rate (float): Ставка штрафа за один день просрочки.
        title (str): Название фильма для формирования понятных логов.

    Returns:
        tuple[float, float] | None: Кортеж (total_fine, return_index),
            если расчет прошел успешно. Если произошла ошибка, возвращает None.
    """
    try:
        # Преобразование дней в float
        numeric_days = float(days_overdue)

        # Расчет показателей
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        return total_fine, return_index

    except ZeroDivisionError as e:
        print(
            f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{title}': {e}"
        )
        return None

    except ValueError as e:
        print(
            f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{title}': {e}"
        )
        return None

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{title}': {e}")
        return None

    finally:
        # Блок выполняется ВСЕГДА при любом исходе
        print("--- Проверка транзакции возврата завершена ---")


# --- Блок тестирования программы ---
if __name__ == "__main__":
    # Входные данные для тестов (исправлен синтаксис [3,])
    test_cases = [
        {"title": "Matrix", "days": 5, "rate": 1.5},
        {"title": "Inception", "days": "пять", "rate": 2.0},
        {"title": "Avatar", "days": 0, "rate": 2.5},
        {"title": "Interstellar", "days": [3, ], "rate": 3.0},
    ]

    print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

    for movie in test_cases:
        # Вызов функции с передачей названия фильма напрямую
        result = calculate_overdue_fine(
            days_overdue=movie["days"],
            fine_rate=movie["rate"],
            title=movie["title"],
        )

        if result:
            # Успешный расчет
            total_fine, return_index = result
            print(
                f"Фильм: '{movie['title']}' | "
                f"Итоговый штраф: {total_fine}$ | "
                f"Индекс: {return_index}"
            )

        # Добавляем пустую строку для красивого разделения тестов в консоли
        print()
