num1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))
if operation == "+":
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == "/":
    if num2 == 0:
        print("Ошибка: деление на ноль невозможно!")
    else:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
else:
    print("Ошибка: неверный знак операции!")
