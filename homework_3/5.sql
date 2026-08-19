-- Выбираем столбец и подсчитываем общее количество записей для каждой из них
SELECT country, COUNT(*) AS count
-- Указываем таблицу
FROM Customers
-- Группируем все строки таблицы по значению в столбце country 
GROUP BY country;
