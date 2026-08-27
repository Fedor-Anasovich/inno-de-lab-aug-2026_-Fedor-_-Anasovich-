--  Создание новой таблицы Departments с предварительным удалением 
--  так как в преведущей попытке уже создавал 
DROP TABLE IF EXISTS Departments CASCADE;

CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);

-- Изменение таблицы Employees добавляем Email, только если его еще нет
ALTER TABLE Employees 
ADD COLUMN IF NOT EXISTS Email VARCHAR(100);

-- Заполнение столбца Email 
UPDATE Employees
SET Email = 'employee' || EmployeeID || '@company.com'
WHERE Email IS NULL;

-- Добавление ограничения UNIQUE к столбцу Email в таблице Employees
-- удаляем старое ограничение , чтобы избежать дубликатов
ALTER TABLE Employees DROP CONSTRAINT IF EXISTS UQ_Employees_Email;

ALTER TABLE Employees 
ADD CONSTRAINT UQ_Employees_Email UNIQUE (Email);

-- Переименование столбца Location в таблице Departments в OfficeLocation
-- Так как на Шаге 1 таблица пересоздается заново, столбец гарантированно называется Location
ALTER TABLE Departments 
RENAME COLUMN Location TO OfficeLocation;