-- Собираем агрегированные данные по заказам
WITH ClientOrders AS (
    SELECT 
        customer_id,
        COUNT(order_id) AS total_orders, -- Считаем чистые заказы
        SUM(amount) AS total_amount       -- Считаем точную сумму без дублей
    FROM Orders
    GROUP BY customer_id
),

-- Считаем количество успешных доставок для каждого клиента
ClientDeliveredShippings AS (
    SELECT 
        customer,
        COUNT(CASE WHEN status = 'Delivered' THEN 1 END) AS delivered_count
    FROM Shippings
    GROUP BY customer
)

-- Объединяем данные клиентов с чистыми агрегатами
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    co.total_orders,
    co.total_amount
FROM Customers c
-- Подключаем предрасчитанные заказы
JOIN ClientOrders co ON c.customer_id = co.customer_id
-- Подключаем предрасчитанные доставки
JOIN ClientDeliveredShippings cds ON c.customer_id = cds.customer
-- Фильтруем итоговый результат
WHERE co.total_orders >= 2           
  AND cds.delivered_count >= 1;      
