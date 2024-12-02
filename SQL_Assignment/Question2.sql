
USE Tech4Girls_DB;

CREATE TABLE IF NOT EXISTS Posts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;

INSERT INTO Posts (user_id, title, content)
VALUES (1, 'Out of this World', 'They say your comfort zone keeps a hold of you so I want to tear down the walls that hold me inside.'),
(2, 'Repose', 'The calmness breeze at the beach helps the mind escape from reality creating a perfect paradise.'),
(2, 'Vitality', 'Its not just about being alive, its about thriving and embracing challenges, and finding joy in every moment'),
(3, 'Assurance', 'Do not worry; you have got this!'),
(1, 'Nature', 'It is a beautiful escape; enjoy its wonders and let it inspire you');


SELECT * FROM Posts;

