requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
required_admin_roles = {"admin", "security_officer", "audit_manager"}
# Удаляем дубликаты
unique_requested = set(requested_roles)
# Пересечение множеств
common_admin_roles = unique_requested.intersection(required_admin_roles)
# Разность множеств
missing_admin_roles = required_admin_roles.difference(unique_requested)
# Проверка наличия роли за время
has_security_officer = "security_officer" in unique_requested
print(f"Уникальные запрошенные роли: {unique_requested}")
print(f"Общие административные роли: {common_admin_roles}")
print(f"Недостающие административные роли: {missing_admin_roles}")
print(f"Наличие роли security_officer в запросе: {has_security_officer}")
