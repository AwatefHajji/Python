from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import show_model
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


#!=========================================CRUD Queries================================================#
    #?==============Create user=================#
    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #?==============Read Queries=================#
                #*===Read all user======#
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users"""
        results= connectToMySQL(DATABASE).query_db(query)
        users=[]
        for row in results:
            users.append(cls(row))
        return users
            #*===Read one by id======#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM users WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
            #*===Read one by email======#
    @classmethod
    def get_by_email(cls, data):
        query = """SELECT * FROM users WHERE email = %(email)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    

    #!=======================================Validation====================================#
    @staticmethod #!!!!!!!! static method juste pour validation
    def validate_user(data):  
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash("Invalid first name, must be greater than 2 characters!", "first_name")

        if len(data['last_name']) < 2:
            is_valid = False
            flash("Invalid last name, must be greater than 2 characters!", "last_name")

        if len(data['email']) < 1:
            is_valid = False
            flash("Email is required", "email")

        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", "email")
            is_valid = False
        else:
            email_dict = {
                'email' : data['email']
            }

            potential_user = User.get_by_email(email_dict)
            if potential_user: #! email is not unique
                is_valid = False
                flash("email already taken ! Please login","email")
        if len(data['password']) < 1:
            is_valid = False
            flash("Invalid password, must be greater than 8 characters!", "password")
        elif not data['password'] == data['confirm_password']:
            is_valid = False 
            flash("Password and confirm_password must match!", "confirm_password")
            

        return is_valid