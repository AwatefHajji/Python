# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
# model the class of the dojos table from our database
class Dojo:

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        #?att to get the part of ninja after Join
        self.ninja_part = []

    @classmethod
    def add_new_dojo(cls,data):
        #! data=request.form is a dictionary that will be passed into the save method from server.py
        query="INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s,NOW(),NOW())"
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(f"+++++++++++++++++++{result}+++++++++++++++++++")
        return result
        # *******show all the dojos in the DB************
    @classmethod
    def get_all_from_DB(cls):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojo_list = []
        if result:
            for row in result:
                one_dojo = cls(row)
                dojo_list.append(one_dojo)
                print(f"!!!!!!!!!!!!!!!!!!!{dojo_list}!!!!!!!!!!!!!!!")
            return dojo_list
        return []
    # ************get one dojo**********
    @classmethod
    def get_one_dojo_from_db(cls,data):
        query="SELECT * from dojos WHERE id = %(id)s;"
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(f"+++++++++kkkkkkk{result}kkkkkkkkkkkk++++++++++")
        return result
#************get dojos and ninjas after Join ***************
    @classmethod
    def get_all_dojo_s_ninja(cls,data):
        query="""SELECT * FROM dojos
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        where dojos.id = %(id)s;
        """
        result=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(f"********////////*******{result}******++++++++++++++++++")
        #?dojo_part = instance d class Dojo with first part d result of Join
        dojo_part=cls(result[0]) 
        for row in result:
            
            #?ninja_new_data = new data for ninja_part where we change names changed after  Join
            ninja_new_data={
                "id": row["ninjas.id"],
                "first_name": row["first_name"],
                "last_name":row["last_name"],
                "age":row["age"],
                "created_at" : row["ninjas.created_at"],
                "updated_at" : row["ninjas.updated_at"]
                
            }
            #?this_ninja = instance d class Ninja with first part d result of Join
            this_ninja=Ninja(ninja_new_data)
            print(f"++++++++{this_ninja}+++++++++++++++")
            #?add this_ninja in the new attr (ninja_part) in the class Dojo
            dojo_part.ninja_part.append(this_ninja)
        return dojo_part

    