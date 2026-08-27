stroka = "   10827  ; aLeXanDer_vLaDimiRov ;   mInSk   ; ACTIVE  "  # исходная строка
#Разбиваем и очищаем элементы в цикле
cleaned_elements = []
for item in stroka.split(";"):
    cleaned_elements.append(item.strip())
uid, name, city, status = cleaned_elements
# Префикс UID- к идентификатору
uid = f"UID-{uid}"
name = name.replace("_", " ").title()
# верхний регистр
city = city.upper()
# нижний регистр
status = status.lower()
# Объединяем и выводим результат
normalized_record = " | ".join([uid, name, city, status])
print(f"Нормализованная запись: {normalized_record}")
