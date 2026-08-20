-- Выбираем столбцы
SELECT order_id, item, amount, customer_id
-- Указываем таблицу
FROM Orders
-- Оставляем только заказы, где сумма строго больше 1000
WHERE amount > 1000;
