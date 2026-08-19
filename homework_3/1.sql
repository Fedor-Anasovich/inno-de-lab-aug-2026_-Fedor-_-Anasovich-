-- Выбираем столбцы
SELECT first_name, last_name, age, country 
-- Указываем таблицу 
FROM Customers 
-- Оставляем только клиентов из США И старше 25 лет
WHERE country = 'USA' AND age > 25;
