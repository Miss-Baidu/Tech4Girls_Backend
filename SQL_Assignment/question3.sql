
USE Tech4Girls_DB;

-- CREATING A TABLE CALLED Courses
CREATE TABLE IF NOT EXISTS Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);


-- CREATING ANOTHER TABLE CALLED User_Courses
CREATE TABLE IF NOT EXISTS User_Courses (
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES  Users(id),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

-- QUERY TO SHOW THAT TABLES HAVE BEEN CREATED IN OUR DATABASE
SHOW TABLES;



-- -- INSERTING VALUES INTO THE Courses TABLES
-- INSERT INTO Courses (course_name)
-- VALUES('Introduction to Engineering'),
-- ('Liear Algebra'),
-- ('Backend Development'),
-- ('Python');

-- -- SELECTING ALL COLUMNS AND ROWS IN THE Courses TABLE TO BE DISPLAYED
-- SELECT * FROM Courses;


-- -- INSERTING VALUES INTO THE User_Courses TABLES
-- INSERT INTO User_Courses (user_id, course_id)
-- VALUES (1, 2),
-- (1, 4),
-- (3, 1),
-- (2, 2),
-- (2, 1),
-- (3, 4),
-- (2, 3);


-- -- SELECTING ALL COLUMNS AND ROWS IN THE Users TABLE TO BE DISPLAYED
-- SELECT * FROM Users;



-- -- SELECTING ALL COLUMNS AND ROWS IN THE User_Courses TABLE TO BE DISPLAYED
-- SELECT * FROM User_Courses; 

