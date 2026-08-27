# Список транзакций
transaction = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]
# Реализация фильтрации в одну строку
valid_amounts = [int(tx.split(":")[1]) for tx in transaction if tx.startswith("SUCCESS:") and int(tx.split(":")[1]) > 0]
print(f"Очищенные транзакции: {valid_amounts}")
