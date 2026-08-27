system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]
# Инициализируем списки
active_nodes = []
cpu_loads = []
ram_usages = []
# Распаковываем кортежи
for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status == "offline":
        continue
    # Собираем данные
    active_nodes.append(node_name)
    cpu_loads.append(cpu_load)
    ram_usages.append(ram_usage)
# Рассчитываем показатели
active_count = len(active_nodes)
avg_cpu = round(sum(cpu_loads) / active_count, 2) if active_count > 0 else 0.0
peak_ram = max(ram_usages) if active_count > 0 else 0
# Формируем словарь
report = {
    'active_nodes_count': active_count,
    'metrics': {
        'average_cpu': avg_cpu,
        'max_ram': peak_ram
    }
}
print(f"Активные узлы в сети: {active_nodes}")
print("Итоговый отчет телеметрии:")
import pprint
pprint.pprint(report, sort_dicts=False)
