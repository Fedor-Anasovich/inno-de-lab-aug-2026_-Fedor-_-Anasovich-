-- Выбираем столбцы
SELECT 
    order_id, 
    customer_id, 
    item, 
    amount,
    -- Оконная функция: считает общую сумму изолируя расчеты по каждому customer_id с помощью PARTITION BY
    SUM(amount) OVER(PARTITION BY customer_id) AS total_by_customer
-- Указываем таблицу 
FROM Orders;
