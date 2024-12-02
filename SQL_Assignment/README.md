# MANAGING DATABASES WITH MySQL: SQL ASSIGNMENT

![Header Image](https://th.bing.com/th/id/OIP.WYatSqYtf98Q6nU3WCHg9gHaHa?rs=1&pid=ImgDetMain)

A Database is a structured collection of data used by backend servers to store, manage, and organize information efficiently. It allows backend code to retrieve, update, and delete data, ensuring smooth application functionality. Data is typically stored in tables, rows, and columns for easy access.

SQL (Structured Query Language) is a language used to interact with relational databases, enabling tasks such as querying, inserting, updating, and deleting data. Key SQL commands include SELECT, INSERT, UPDATE, and DELETE.

MySQL is an open-source relational database management system (RDBMS) that uses SQL to manage data. Known for its high performance, security, and scalability, MySQL is widely used in web applications and is a vital tool for backend development.

## Author
* [Sarah Baidu](http://linkedin.com/in/sarah-baidu-0281a4260)


## Submission Synopsis: SQL Assignment

This repository contains SQL code for an assignment designed to provide hands-on experience in managing data within a relational database. The key objectives of the assignment are:

1. Create a database
2. Select and use the database
3. Design and create tables
4. Insert data into the tables
5. Query and retrieve all columns and rows from a table
6. Establish a One-to-Many relationship between tables by referencing a column in another table
7. Implement a Many-to-Many relationship between tables using foreign keys

The project is structured to help us grasp fundamental database concepts, including creating and managing databases, defining tables, inserting data, querying tables, and performing data modifications such as updating or deleting records.

Additionally, the project focuses on understanding how to establish relationships between tables in a database, specifically by using foreign keys to link columns from one table to another.

## How to Use This Repository

```bash
  # Clone the repository to your local machine.
  git clone https://github.com/Miss-Baidu/Tech4Girls_Backend.git

  # Navigate to the directory where you cloned it.
  cd SQL_Assignment 

  # Run the provided SQL scripts in your terminal.
  mysql -u root -p 

  # Follow the prompts in each script to interact with the programs.


## Submission Structure

This submission includes the following files and directories:

- **question1.sql**: Creates a database and populates a table with initial values.
- **question2.sql**: Creates a new table and establishes a one-to-many relationship with the table from **question1.sql**.
- **question3.sql**: Creates another table and defines a many-to-many relationship between the table from **question1.sql** and the table in this file.

Objectives:
Create a Database and Use it
Create tables and insert values into them
Establish relationships between tables using foreign keys

Here is a rephrased, edited, and summarized version:

## Aspects

### Database Creation:
- The **question1.sql** script creates a database if it doesn't already exist:
```bash
CREATE DATABASE IF NOT EXISTS Tech4Girls_DB;
```

### Table Creation:
- The SQL scripts define tables, for example, creating a **Users** table:
```bash
CREATE TABLE IF NOT EXISTS Users (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50),
  email VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Inserting Values into Tables:
- The scripts insert sample values into tables. For example, inserting data into the **Users** table:
```bash
INSERT INTO Users (username, email)
VALUES ('Ama', 'ama@example.com'),
       ('Abena', 'abena@example.com'),
       ('Adjoa', 'adjoa@example.com');
```

### Selecting All Columns and Rows:
- The following query retrieves all columns and rows from the **Users** table:
```bash
SELECT * FROM Users;
```

### Establishing Relationships with Foreign Keys:
- The **Posts** table is created, and a foreign key relationship is established between the **Users** and **Posts** tables:
```bash
CREATE TABLE IF NOT EXISTS Posts (
  id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Users(id),
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tech Stack:
- **SQL**: Structured Query Language
- **MySQL**: Relational database management system

This structure follows a logical flow of creating a database, tables, inserting values, selecting data, and establishing relationships between tables.
