from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
from flask import flash

class Dojo:

    def __init__(self, data):

        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ======== CREATE DOJO ==========
    @classmethod 
    def create(cls, data):

        query = """
                INSERT INTO dojos (name, location, language, comment)
                VALUES (%(name)s,%(location)s,%(language)s,%(comment)s) ;
                """
        
        return MySQLConnection(DATABASE).query_db(query, data)
    
    # ======== FIND DOJO BY ID ==========
    @classmethod
    def get_by_id(cls, data):

        query = """
                SELECT * FROM dojos
                WHERE id = %(id)s ;
                """
        result = MySQLConnection(DATABASE).query_db(query, data)
        if len(result) < 1:
            return []
        return cls(result[0])
    
    #! ========= Vadition ===============

    @staticmethod
    def validate_reg(data):

        is_valid = True
        if len(data['name']) < 1:
            is_valid = False
            flash("Name must be at least 3 caracters", "registration")

        if len(data['location']) < 1:
            is_valid = False
            flash("Must choose a Dojo Location ", "registration")

        if len(data['lang']) < 1:
            is_valid = False
            flash("You must choose your favorite Language", "registration")

        if len(data['comment']) < 1:
            is_valid = False
            flash("Comment must be at least 3 caracters", "registration")

        return is_valid