-- Create Database
CREATE DATABASE EmployeeDB;

-- Use the newly created database
USE EmployeeDB;

-- Create Employees Table
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    department VARCHAR(255) NOT NULL,
    salary FLOAT NOT NULL
);

-- Insert Sample Data
INSERT INTO employees (name, age, jobprofile, salary) VALUES ('rahul', 30, 'HR', 50000);
INSERT INTO employees (name, age, jobprofile, salary) VALUES ('shreyash', 21, 'software engineer', 60000);
INSERT INTO employees (name, age, jobprofile, salary) VALUES ('praveen', 21, 'IT', 70000);
INSERT INTO employees (name, age, jobprofile, salary) VALUES ('prashant', 21, 'software engineer', 55000);

-- Verify the inserted data
SELECT * FROM employees;
