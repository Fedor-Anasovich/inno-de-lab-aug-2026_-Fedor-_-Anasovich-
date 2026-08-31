import io
import sys
from typing import Any, Optional, Tuple

# Константа на уровне модуля
DEFAULT_RETURN_INDEX_BASE = 10.0


# Реализация функции с безопасной обработкой исключений
def calculate_overdue_fine(
    days_overdue: Any, fine_rate: float
) -> Optional[Tuple[float, float]]:
    """Рассчитывает сумму штрафа и технический индекс оборачиваемости фильма.

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

    Returns:
        Optional[Tuple[float, float]]: Кортеж (total_fine, return_index),
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
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки: {e}")
        return None

    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число: {e}")
        return None

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных: {e}")
        return None

    finally:
        # Блок выполняется ВСЕГДА при любом исходе
        print("--- Проверка транзакции возврата завершена ---")


# --- Блок тестирования программы ---
if __name__ == "__main__":
    # Входные данные для тестов (Синтаксис исправлен на [3,])
    test_cases = [
        {"title": "Matrix", "days": 5, "rate": 1.5},
        {"title": "Inception", "days": "пять", "rate": 2.0},
        {"title": "Avatar", "days": 0, "rate": 2.5},
        {"title": "Interstellar", "days": [3,], "rate": 3.0},
    ]

    print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

    for movie in test_cases:
        # Перенаправляем stdout, чтобы красиво встроить имя фильма в текст ошибки
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        # Вызов функции
        result = calculate_overdue_fine(movie["days"], movie["rate"])

        # Возвращаем стандартный вывод
        sys.stdout = old_stdout
        output = new_stdout.getvalue().strip().split("\n")

        if result:
            # Успешный расчет
            total_fine, return_index = result
            print(
                f"Фильм: '{movie['title']}' | "
                f"Итоговый штраф: {total_fine}$ | "
                f"Индекс: {return_index}"
            )
            print(output[-1])  # Печатаем строку из finally
        else:
            # Ошибка: форматируем вывод под требования задания
            err_msg = output[0]
            if "[ОШИБКА ЗНАЧЕНИЯ]" in err_msg:
                err_msg = err_msg.replace(
                    "число:", f"число для '{movie['title']}':"
                )
            elif "[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ]" in err_msg:
                err_msg = err_msg.replace(
                    "просрочки:", f"просрочки для '{movie['title']}':"
                )
            elif "[ОШИБКА ТИПА]" in err_msg:
                err_msg = err_msg.replace(
                    "данных:", f"данных для '{movie['title']}':"
                )

            print(err_msg)
            print(output[-1])  # Печатаем строку из finally
