INSERT INTO Employees (FirstName, LastName, Department, Salary)
VALUES 
('John', 'Doe', 'Sales', 50000.00),
('Anna', 'Nova', 'HR', 45000.00);

SELECT * FROM Employees;

SELECT FirstName, LastName 
FROM Employees 
WHERE Department = 'IT';

UPDATE Employees
SET Salary = 65000.00
WHERE FirstName = 'Alice' AND LastName = 'Smith';

DELETE FROM Employees
WHERE FirstName = 'Eve' AND LastName = 'Davis';

SELECT * FROM Employees;