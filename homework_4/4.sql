
--  Увеличить Salary всех сотрудников в отделе 'HR' на 10%
UPDATE Employees 
SET Salary = Salary * 1.10 
WHERE Department = 'HR';

-- Обновить Department любого сотрудника с Salary выше 70000.00 на 'Senior IT'
UPDATE Employees 
SET Department = 'Senior IT' 
WHERE Salary > 70000.00;

-- Удалить всех сотрудников, которые не назначены ни на один проект
DELETE FROM Employees e
WHERE NOT EXISTS (
    SELECT 1 
    FROM EmployeeProjects ep 
    WHERE ep.EmployeeID = e.EmployeeID
);

BEGIN;

INSERT INTO Projects (ProjectName, Budget, StartDate) 
VALUES ('New Automation Project', 50000.00, CURRENT_DATE);

-- Назначаем двух существующих сотрудников. 
-- В поле HoursWorked передаем целые числа 40 и 25.
INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
VALUES 
((SELECT EmployeeID FROM Employees ORDER BY EmployeeID ASC LIMIT 1), (SELECT MAX(ProjectID) FROM Projects), 40),
((SELECT EmployeeID FROM Employees ORDER BY EmployeeID ASC OFFSET 1 LIMIT 1), (SELECT MAX(ProjectID) FROM Projects), 25);

COMMIT;

SELECT * FROM Employees; 
SELECT * FROM EmployeeProjects;
