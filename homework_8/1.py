# Константа на уровне модуля
MAX_RENTAL_BATCH_LIMIT = 150.0


# Определение функции с Type Hints и Google Docstring
def calculate_rental_batch(
    quantity: int, rental_rate: float, discount: float = 0.0
) -> tuple[float, bool]:
    """Рассчитывает финальную стоимость аренды партии и проверяет превышение лимита.

    Args:
        quantity (int): Количество арендуемых единиц.
        rental_rate (float): Базовая стоимость аренды за одну единицу.
        discount (float, optional): Процент скидки в виде десятичной дроби
            (например, 0.1 для 10%). Значение по умолчанию: 0.0.

    Returns:
        tuple[float, bool]: Кортеж, содержащий:
            - final_sum (float): Итоговая стоимость аренды, округленная до двух
              знаков после запятой.
            - is_limit_exceeded (bool): Флаг превышения лимита. True, если
              итоговая стоимость больше MAX_RENTAL_BATCH_LIMIT, иначе False.
    """
    # Логика расчета стоимости и проверки лимита
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum > MAX_RENTAL_BATCH_LIMIT
    return final_sum, is_limit_exceeded


# Демонстрация работы и формирование отчета
# Тестовые данные по партиям
batches = [
    {
        "name": "Academy Dinosaur",
        "args": (30, 2.99),
        "kwargs": {},
        "call_type": "positional",
    },
    {
        "name": "Affair Prejudice",
        "args": (40, 4.99),
        "kwargs": {"discount": 0.1},
        "call_type": "mixed",
    },
    {
        "name": "Agent Truman",
        "args": (),
        "kwargs": {"quantity": 10, "rental_rate": 1.99},
        "call_type": "keyword",
    },
    {
        "name": "African Egg",
        "args": (50, 3.50, 0.2),
        "kwargs": {},
        "call_type": "positional",
    },
]

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")
for idx, batch in enumerate(batches, 1):
    # Демонстрация разных способов вызова функции по требованию задания
    if batch["call_type"] == "positional":
        # Вызов с позиционными аргументами
        final_sum, is_limit_exceeded = calculate_rental_batch(*batch["args"])
    elif batch["call_type"] == "keyword":
        # Вызов с именованными аргументами
        final_sum, is_limit_exceeded = calculate_rental_batch(**batch["kwargs"])
    else:
        # Смешанный вызов (позиционные + именованные)
        final_sum, is_limit_exceeded = calculate_rental_batch(
            *batch["args"], **batch["kwargs"]
        )

    print(
        f"Партия {idx} ({batch['name']}): Сумма {final_sum}$. "
        f"Превышение лимита: {is_limit_exceeded}"
    )
