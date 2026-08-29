
--  Создание роли hr_user с возможностью входа и паролем
CREATE ROLE hr_user WITH LOGIN PASSWORD 'secure_password123';

--  Предоставление ТОЛЬКО прав SELECT на таблицу Employees
GRANT SELECT ON Employees TO hr_user;

SET ROLE hr_user;

-- Проверка чтения данных 
SELECT * FROM Employees;
INSERT INTO Employees (FirstName, LastName, Department, Salary) 
VALUES ('Test', 'User', 'HR', 40000.00);

RESET ROLE; 

-- Предоставление дополнительных прав INSERT и UPDATE
GRANT INSERT, UPDATE ON Employees TO hr_user;

SET ROLE hr_user;

INSERT INTO Employees (FirstName, LastName, Department, Salary) 
VALUES ('Olga', 'Petrova', 'HR', 48000.00);

UPDATE Employees 
SET Salary = 52000.00 
WHERE FirstName = 'Olga' AND LastName = 'Petrova';

RESET ROLE;
