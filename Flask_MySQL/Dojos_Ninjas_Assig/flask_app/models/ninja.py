# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class of the ninjas table from our database
class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"] 
        self.updated_at = data["updated_at"]
    @classmethod
    def add_new_ninja(cls,data):
        #! data=request.form is a dictionary that will be passed into the save method from server.py
        query="INSERT INTO ninjas (first_name,last_name,age,dojo_id,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s,NOW(),NOW())"
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(f"+++++++++++++++++++{result}+++++++++++++++++++")
        return result
    @classmethod
    def get_one_ninja(cls,data):
        query="SELECT * FROM ninjas where id =%(id)s ;"
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        this_ninja=cls(result[0])
        print(f"+++++++++++++++++++{result}+++++++++++++++++++")
        return this_ninja
    @classmethod
    def edit_ninja(cls,data):
        query="UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s, age=%(age)s,updated_at=NOW() WHERE id= %(id)s"
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(f"+++++++++++++++++++{result}+++++++++++++++++++")
        return result

