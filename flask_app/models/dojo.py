from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo():
    
    def __init__(self, data):
        self.id = data['id']
        self.location_name = data['location_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
        
    @classmethod
    def create_dojo(cls, data):
        
        query = "INSERT INTO dojos (location_name) VALUES (%(location_name)s);"
        
        new_dojo_id = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        # returns the int of id number
        
        return new_dojo_id
    
    @classmethod 
    def get_all_dojos(cls):
        
        query = "SELECT * FROM dojos;"
        
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
    
        dojos = []
        
        for item in results:
            new_item = Dojo(item)
            dojos.append(new_item)

        return dojos
    
    @classmethod
    def get_dojo_by_id(cls, data):

        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)

        print(results)

        dojo = Dojo(results[0])

        for item in results:
            if item['ninjas.id'] != None:
                ninja_data = {
                    'id': item['ninjas.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'age': item['age'],
                    'created_at':item['created_at'],
                    'updated_at': item['updated_at'],
                    'dojo_id': item['dojo_id'] 
                }
                ninja = Ninja(ninja_data)
                ninja.dojo = dojo
                dojo.ninjas.append(ninja)

        return dojo


    @classmethod
    def get_all_dojos_with_ninjas(cls):
        
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id;"
        
        results = connectToMySQL('dojos_and_ninjas').query_db(query)

        dojos = []
        
        for item in results:
            if len[dojos] == 0:
                new_dojo = Dojo(item)
                dojos.append(new_dojo)
            elif dojos[-1].id != item['id']:
                new_dojo = Dojo(item)
                dojos.append(new_dojo)
            if item['ninjas.id'] != None:
                ninja_data = {
                    'id': item['ninjas.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'age': item['age'],
                    'created_at':item['created_at'],
                    'updated_at': item['updated_at'],
                    'dojo_id': item['dojo_id'] 
            }
                ninja = Ninja(ninja_data)
                ninja.dojo = new_dojo
                new_dojo.ninjas.append(ninja)

        return dojos