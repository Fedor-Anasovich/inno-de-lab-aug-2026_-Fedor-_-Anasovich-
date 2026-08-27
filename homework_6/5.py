import random
number = random.randint(1, 20)
attem = 5
print("Я загадал число от 1 до 20. Попробуй угадать его за 5 попыток!")
while attem > 0:
    gue = int(input(message := f"\n(Осталось попыток: {attem}). Введите ваше число: "))
    if gue == number:
        print(f"Поздравляю! Вы угадали число {number}!")
        break
    elif gue > number:
        print("Слишком много!")
    else:
        print("Слишком мало!")
    attem -= 1
if attem == 0:
    print(f"\nК сожалению, попытки закончились. Я загадал число {number}.")
