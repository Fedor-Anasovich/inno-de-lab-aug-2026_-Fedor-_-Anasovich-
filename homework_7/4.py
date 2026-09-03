# Исходный список ролей, полученный из запроса. Содержит повторяющиеся элементы (дубликаты).
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]

# Множество эталонных административных ролей, которые требуются для полной проверки доступа.
# Множества задаются фигурными скобками {} и содержат только уникальные элементы.
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# Удаляем дубликаты из исходного списка, преобразуя его в множество с помощью функции set().
# Множество автоматически отбросит все повторяющиеся строки "guest" и "developer".
# Порядок элементов при этом не гарантируется.
unique_requested = set(requested_roles)

# Пересечение множеств (Intersection).
# Метод .intersection() находит элементы, которые одновременно присутствуют
# и в множестве unique_requested, и в множестве required_admin_roles (то есть их общую часть).
common_admin_roles = unique_requested.intersection(required_admin_roles)

# Разность множеств (Difference).
# Метод .difference() возвращает элементы из required_admin_roles, которых НЕТ в unique_requested.
# Это позволяет нам четко увидеть, каких именно обязательных админ-ролей не хватает в запросе.
missing_admin_roles = required_admin_roles.difference(unique_requested)

# Проверка наличия конкретного элемента с помощью оператора 'in'.
# Операция 'in' для множеств выполняется мгновенно (за константное время O(1)),
# в отличие от списков, где Python перебирал бы каждый элемент по очереди.
has_security_officer = "security_officer" in unique_requested

# Выводим результаты работы программы в консоль.
print(f"Уникальные запрошенные роли: {unique_requested}")
print(f"Общие административные роли: {common_admin_roles}")
print(f"Недостающие административные роли: {missing_admin_roles}")
print(f"Наличие роли security_officer в запросе: {has_security_officer}")
