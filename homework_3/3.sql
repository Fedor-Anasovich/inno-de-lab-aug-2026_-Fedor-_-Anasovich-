-- Выбираем столбцы
SELECT c.first_name, c.last_name, o.item, o.amount
-- Указываем таблицу и задаем псевдоним "o"
FROM Orders o
-- Внутренним соединением (JOIN) подключаем таблицу Customers (Клиенты) с псевдонимом "c"
JOIN Customers c 
  -- Задаем условие связи: ID клиента в заказах должен совпадать с ID клиента в базе клиентов
  ON o.customer_id = c.customer_id;
