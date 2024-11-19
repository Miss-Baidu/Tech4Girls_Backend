-- an sql script that teaches sql commands; single line comment
CREATE DATABASE  IF NOT EXISTS tech4girls;
SHOW DATABASES;
USE tech4girls;

CREATE TABLE IF NOT EXISTS backend_class (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(256),
    age INT,
    email VARCHAR(256) UNIQUE NOT NULL
);

SHOW TABLES;

INSERT INTO backend_class (first_name, last_name, age, email)
VALUES('Sara', 'Baidu', 20, 'akuabaidu16@gmail.com');

SELECT * FROM backend_class