config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}
# Извлекаем значения host и port
conn_dict = config.get("connection", {})
host = conn_dict.get("host")
port = conn_dict.get("port")

# Проверяем наличие ssl_settings и ssl_mode с дефолтным значением
ssl_mode = config.get("ssl_settings", {}).get("ssl_mode", "verify-full")
conn_dict["user"] = "admin"
conn_dict["max_connections"] = 100
print(f"SSL Mode: {ssl_mode}")
print("Параметры соединения:")

# Итерация по парам словаря через .items()
for key, value in conn_dict.items():
    print(f"* {key}: {value}")
