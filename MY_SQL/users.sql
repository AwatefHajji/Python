INSERT INTO users (first_name, last_name,email) 
VALUES('awatef', 'hajji','awa@gmail.com'),('asma', 'hajji','asma@gmail.com'),('afef', 'haj','afef90@gmail.com');
select * from users;
select *
from users
where email='awa@gmail.com';
select *
from users
where id=3;
UPDATE users
SET last_name = 'Litime'
WHERE id=3;
select * from users;
SET SQL_SAFE_UPDATES = 0;
DELETE FROM users WHERE id=2;
select id,first_name
from users
order by id desc