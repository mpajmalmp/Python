CREATE DATABASE OnlineBookstore;
USE OnlineBookstore;

CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT,
    price DECIMAL(10, 2),
    publication_year INT,
    genre VARCHAR(50),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    customer_name VARCHAR(100),
    order_date DATE,
    quantity INT,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

INSERT INTO authors (author_name, country) 
VALUES 
('Rajesh', 'India'),
('Ramesh', 'India'),
('Arjun', 'India');

INSERT INTO books (title, author_id, price, publication_year, genre) 
VALUES 
('Wings', 1, 20, 1998, 'Autobiography'),
('Indiana', 2, 35, 1989, 'Drama'),
('Bedtime stories', 3, 22, 1991, 'Fiction');

INSERT INTO orders (book_id, customer_name, order_date, quantity) 
VALUES 
(1, 'Alice Johnson', '2025-01-10', 2),
(2, 'Bob Smith', '2025-01-15', 1),
(3, 'Charlie Lee', '2025-01-20', 3);


SELECT * FROM books;

SELECT * FROM authors;

SELECT * FROM orders;

ALTER TABLE books 
ADD COLUMN genre VARCHAR(50);

ALTER TABLE orders 
ADD COLUMN quantity INT;

SELECT b.book_id, b.title, b.price, b.publication_year, b.genre, a.author_name, a.country
FROM books b
JOIN authors a ON b.author_id = a.author_id;

SELECT o.order_id, o.customer_name, o.order_date, o.quantity, b.title 
FROM orders o
JOIN books b ON o.book_id = b.book_id;
