MySQL Advanced
Overview
This project focuses on advanced SQL concepts and practices using MySQL. You will work with various SQL functionalities such as creating tables with constraints, optimizing queries with indexes, implementing stored procedures, functions, views, and triggers in MySQL.

Concepts Covered
Creating tables with constraints
Optimizing queries by adding indexes
Implementing stored procedures and functions
Implementing views
Implementing triggers
Resources
MySQL cheatsheet
MySQL Performance: How To Leverage MySQL Database Indexing
Stored Procedure
Triggers
Views
Functions and Operators
Trigger Syntax and Examples
CREATE TABLE Statement
CREATE PROCEDURE and CREATE FUNCTION Statements
CREATE INDEX Statement
CREATE VIEW Statement
Usage
Start MySQL in the container:
bash
Copy code
$ service mysql start
Connect to MySQL via SSH or WebTerminal with credentials root/root.
Import a SQL dump:
bash
Copy code
$ echo "CREATE DATABASE your_database_name;" | mysql -uroot -p
$ curl "https://s3.amazo
