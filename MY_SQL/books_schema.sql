SELECT * FROM books_schema.books;

INSERT INTO users (name)
VALUES ('Jane Amesden'),('Emily Dixon'),('Theodore Destoevsky'),('William Shapiro'),('Lao Xiu');

INSERT INTO books (title)
VALUES ('C charp'),('Java'),('Python'),('PHP'),('Ruby');
SET SQL_SAFE_UPDATES = 0;
UPDATE books SET Title = 'C#'
Where id =1;

UPDATE users SET name = 'Bill'
Where id =4;

INSERT into favorites (user_id, book_id) 
VALUES (1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4), (4,5);

SELECT users.name FROM users
JOIN favorites on users.id = user_id
JOIN books on favorites.book_id = books.id
WHERE books.id = 3;

DELETE from favorites
where book_id = 3 AND user_id = 1;

INSERT into favorites (user_id, book_id) 
VALUES (5, 2);

SELECT title from books
JOIN favorites as fav_book on fav_book.book_id = books.id
WHERE fav_book.user_id = 3;

SELECT name from users
JOIN favorites on users.id = favorites.user_id
WHERE favorites.book_id = 5;

