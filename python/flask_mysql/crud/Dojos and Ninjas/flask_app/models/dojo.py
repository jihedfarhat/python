from flask_app.config.mysqlconnection import connectToMySQL, DATABASE_NAME

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_dojo_by_id(cls , data):
        query = """
            SELECT * FROM dojos WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE_NAME).query_db(query , data)
        if result:
            return cls(result[0])
        return False

    @classmethod
    def get_dojos(cls):
        query = """
            SELECT * FROM dojos;
        """
        result = connectToMySQL(DATABASE_NAME).query_db(query)
        dojos = []
        if(result):
            for item in result:
                dojos.append(cls(item))
        return dojos
    
    @classmethod
    def create_dojo(cls, data):
        query = """
            INSERT INTO dojos (name) VALUES(%(name)s);
        """
        result = connectToMySQL(DATABASE_NAME).query_db(query, data)
        return result