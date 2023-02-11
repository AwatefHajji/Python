# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class of the users table from our database
class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"] 
        self.updated_at = data["updated_at"]
    # *******show all the users in the DB************
    @classmethod
    def get_all_from_DB(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        result = connectToMySQL('users_schemas').query_db(query)
        user_list = []
        if result:

            for row in result:
                # print(f" ====== \n {cls(row).id[0]} \n ======== \n")
                one_user = cls(row)
                user_list.append(one_user)

            return user_list

        return []

    # **************add a new user to the DB****************
    @classmethod
    def save(cls,data):
        #! data=request.form is a dictionary that will be passed into the save method from server.py
        query=" INSERT INTO users (first_name,last_name,email,created_at,updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,NOW(),NOW());"
        results=connectToMySQL('users_schemas').query_db(query,data)
        print(results)
        return results
    
    # *******show one from the users in the DB with id************
    @classmethod
    def get_one_from_DB(cls,data):
        query="SELECT * from users WHERE id = %(id)s"
        result=connectToMySQL('users_schemas').query_db(query,data)
        print(result)
        this_user=cls(result[0])
        return this_user
    # ***************edit user**********
    @classmethod
    def Edit_one_user(cls,data):
        query="UPDATE users SET first_name = %(first_name)s, last_name= %(last_name)s, email= %(email)s, updated_at=NOW() WHERE id = %(id)s;"
        result=connectToMySQL('users_schemas').query_db(query,data)
        print(f"++++++++++++{result}++++++++++++++")
        return result
    @classmethod
    def delete(cls,data):
        query="DELETE FROM users WHERE id =%(id)s;"
        result=connectToMySQL('users_schemas').query_db(query,data)
        print(f"!!!!!!!!!!!!!!!!!++++++++++++{result}++++++++++++++!!!!!!!!!!!!")
        return result
    

