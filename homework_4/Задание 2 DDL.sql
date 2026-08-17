CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);

ALTER TABLE Employees 
ADD COLUMN Email VARCHAR(100);

UPDATE Employees SET Email = 'alice.smith@company.com' WHERE FirstName = 'Alice' AND LastName = 'Smith';
UPDATE Employees SET Email = 'bob.jones@company.com' WHERE FirstName = 'Bob' AND LastName = 'Jones';
UPDATE Employees SET Email = 'john.doe@company.com' WHERE FirstName = 'John' AND LastName = 'Doe';
UPDATE Employees SET Email = 'anna.nova@company.com' WHERE FirstName = 'Anna' AND LastName = 'Nova';
UPDATE Employees SET Email = 'eve.davis@company.com' WHERE FirstName = 'Eve' AND LastName = 'Davis';

ALTER TABLE Employees 
ADD CONSTRAINT UQ_Employees_Email UNIQUE (Email);

ALTER TABLE Departments 
RENAME COLUMN Location TO OfficeLocation;
