# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
  def __init__( self , data ):
    self.id = data['id']
    self.first_name = data['first_name']        
    self.last_name = data['last_name']
    self.email = data['email']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
  
  @classmethod
  def get_all(cls):
    query = "SELECT * FROM users;"
    results = connectToMySQL('users_schemas').query_db(query)
    print(results)
    users = []
    for user in results:
      users.append(cls(user))
    return users
  # ********show one user**********
  @classmethod
  def get_one(cls):
    query = "SELECT * FROM users WHERE id= %(id)s"
    result = connectToMySQL('users_schemas').query_db(query)

    if result:
      users = cls(result[0])
      return users
    return []

# ********create one user**********
  # ============ CREATE ==============
  @classmethod
  def save(cls, data):
    query = """
    INSERT INTO users (first_name, last_name, email, created_at, update_at)
    VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());
    """
    result = connectToMySQL('users_schemas').query_db(query, data)
   
    return result
