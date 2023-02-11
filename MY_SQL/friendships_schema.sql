SELECT * FROM friendships_schema.users;
SELECT * FROM friendships_schema.friendships;
INSERT INTO users (first_name,last_name)
VALUES ('Meriem','Hajji'),('Noua','Hajji'),('Joud','Hajji'),('Chafik','Mgadmini');
INSERT INTO users (first_name,last_name)
VALUES ('Arij','Ounissi');
INSERT INTO friendships (user_id,friend_id)
VALUES (1,2),(1,4),(1,6);
INSERT INTO friendships (user_id,friend_id)
VALUES (2,1),(2,3),(2,5);
INSERT INTO friendships (user_id,friend_id)
VALUES (3,2),(3,5);
INSERT INTO friendships (user_id,friend_id)
VALUES (4,3);
INSERT INTO friendships (user_id,friend_id)
VALUES (5,1),(5,6);
INSERT INTO friendships (user_id,friend_id)
VALUES (6,2),(6,3);
SELECT * FROM users 
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;

SELECT users.first_name , users.last_name ,users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users 
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id;

SELECT users.first_name , users.last_name ,users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users 
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE users.id = 1;

SELECT count(*) as number_friendships FROM friendships;

SELECT users.first_name , users.last_name ,count(user_id) as number_friendships FROM users 
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
group by users.id
LIMIT 1;

SELECT users.id,users.first_name as friends, users2.first_name as first_name, users2.last_name as last_name FROM users 
JOIN friendships ON users.id=friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE users.id =3
ORDER BY first_name;