-- Выбираем столбцы
SELECT c.first_name, c.last_name, o.amount
-- Указываем таблицу и даем ей псевдоним "o"
FROM Orders o
-- Объединяем с таблицей Customers 
JOIN Customers c ON o.customer_id = c.customer_id
-- Фильтруем заказы
WHERE o.amount = (SELECT MAX(amount) FROM Orders);
