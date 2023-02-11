
INSERT INTO dojos (name) 
VALUES('dojo1'),('dojo2'),('dojo3');

INSERT INTO ninjas (first_name,last_name,age,dojo_id) 
VALUES('adam','smith',25,13),('asma','zen',30,13),('myriam','aziz',20,13);

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Sana","Hazem",25,14),("Noua","Jaleli",23,14),("Joud","Sassi",33,14);

INSERT INTO ninjas (first_name,last_name,age,dojo_id)
VALUES ("Mouhamed","Lani",44,15),("Salem","Mahjoub",50,15),("Mouez","Lamred",38,15);

SELECT *
FROM ninjas
WHERE dojo_id=15;


SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 13;

SELECT * FROM dojos
LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
	WHERE dojos.id = (SELECT id FROM dojos ORDER BY id ASC LIMIT 1);
    
SELECT * FROM dojos
WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);