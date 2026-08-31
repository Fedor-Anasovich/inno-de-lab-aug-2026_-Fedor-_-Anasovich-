import functools
import time
# Используем классические Dict, List и Union 
from typing import Any, Callable, Dict, List, Union

# Константы на уровне модуля
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

# Аннотация данных о выручке жанров (
GenreSalesData = List[Dict[str, Union[str, float]]]


# Кастомный декоратор для замера времени выполнения
def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    """Декоратор для автоматического замера и логирования времени работы функции.

    Args:
        func (Callable[..., Any]): Целевая функция, производительность которой
            необходимо измерить.

    Returns:
        Callable[..., Any]: Обернутая функция (wrapper), сохраняющая метаданные
            оригинальной функции.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        execution_time = time.perf_counter() - start_time

        # Вывод сообщения в консоль с заданной точностью TIME_DECIMALS
        print(
            f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' "
            f"выполнена за {execution_time:.{TIME_DECIMALS}f} сек."
        )
        return result

    return wrapper


# 5. Основная функция отчета, обернутая декоратором
@performance_logger
def get_sorted_report(data: GenreSalesData) -> GenreSalesData:
    """Сортирует данные по выручке жанров кинопроката по убыванию.

    Args:
        data (GenreSalesData): Список словарей с информацией о категориях
            и их выручке.

    Returns:
        GenreSalesData: Новый отсортированный список словарей по убыванию
            ключа 'total_sales'.
    """
    # Сортировка по убыванию total_sales с использованием lambda-выражения
    return sorted(data, key=lambda item: float(item["total_sales"]), reverse=True)


# --- Блок тестирования программы ---
if __name__ == "__main__":
    # Входные данные для тестов
    test_cases = [
        # Набор 1 (Стандартный)
        [
            {"category": "Action", "total_sales": 4311.85},
            {"category": "Animation", "total_sales": 4656.30},
            {"category": "Children", "total_sales": 3655.55},
        ],
        # Набор 2 (С одинаковой выручкой)
        [
            {"category": "Classics", "total_sales": 1200.10},
            {"category": "Comedy", "total_sales": 4000.00},
            {"category": "Documentary", "total_sales": 4000.00},
        ],
        # Набор 3 (Единичный элемент)
        [{"category": "Drama", "total_sales": 500.00}],
    ]

    print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

    for idx, test_data in enumerate(test_cases, 1):
        print(f"--- ТЕСТ {idx} ---")
        # Вызов функции с автоматическим логированием времени
        sorted_report = get_sorted_report(test_data)

        print("Топ категорий по выручке:")
        for rank, item in enumerate(sorted_report, 1):
            print(f"{rank}. {item['category']}: {item['total_sales']}")
