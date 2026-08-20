-- Выбираем столбцы
SELECT s.status, c.first_name, c.last_name
-- Указываем таблицу и задаем ей псевдоним "s"
FROM Shippings s
-- Подключаем таблицу под псевдонимом "c"
JOIN Customers c 
  -- Задаем условие связи: поле customer в доставках должно совпадать с customer_id в клиентах
  ON s.customer = c.customer_id;
