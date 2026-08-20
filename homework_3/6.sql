-- Выбираем название товара, считаем количество его продаж и средний чек округляя до 2 знаков
SELECT item, 
       COUNT(*) AS count, 
       ROUND(AVG(amount), 2) AS avg_amount
--  Указываем таблицу 
FROM Orders
-- Группируем все заказы по названию товара 
GROUP BY item;
