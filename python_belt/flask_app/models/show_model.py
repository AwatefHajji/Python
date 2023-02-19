from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model
from datetime import datetime
import re
from flask_app import DATABASE

class Show:
    def __init__(self,data):
        self.id=data["id"]
        self.title=data["title"]
        self.user_id = data['user_id']
        self.network=data["network"]
        self.release_date=data["release_date"]
        self.description=data["description"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.us = []
        self.owner = user_model.User.get_by_id({'id':self.user_id})

    # @staticmethod
    # def get_month_name(date_str):
    #     date = datetime.strptime(date_str, '%Y/%m/%d')
    #     return date.strftime('%B')




    @classmethod
    def create_show(cls,data):
        query="""
        INSERT INTO shows (user_id,title,network,release_date,description)
        VALUES (%(user_id)s,%(title)s,%(network)s,%(release_date)s,%(description)s)"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
#? get all users with shows
    @classmethod
    def get_all_user_show(cls): 
        query = """SELECT * FROM shows 
                   LEFT JOIN users on shows.user_id= users.id """
        results= connectToMySQL(DATABASE).query_db(query)
        these_shows=[]
        
        for row in results:
            this_show = cls(row)

            user_data = {
                **row,
                'id': row['users.id']
            }

            this_user = user_model.User(user_data)
            this_show.us = this_user

            these_shows.append(this_show)

        return these_shows
        

#?get show by id
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM shows WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
#?update show
    @classmethod
    def update(cls, data):
        query = """UPDATE shows
         SET title = %(title)s,network =%(network)s, release_date=%(release_date)s ,description = %(description)s
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
#?delete show
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM shows
         WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod #!!!!!!!! static method for validation
    def validate_show(data):
        is_valid = True
        if len(data["title"])<3:
            is_valid = False
            flash("Invalid title, must be at least 3 characters!", "title")
        if len(data['description']) < 3 :
            is_valid = False
            flash("description must not be blank and must be at least 3 characters!", "description")
        if len(data['network'])<3:
            is_valid = False
            flash("network must be at least 3 characters!", "network")
        if len(data['release_date'])=="":
            is_valid = False
            flash("You should pick a release date", "release_date")
        return is_valid
