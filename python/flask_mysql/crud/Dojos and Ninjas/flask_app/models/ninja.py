from flask_app.config.mysqlconnection import connectToMySQL,DATABASE_NAME

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_by_dojo_id(cls,data):
        query = """
            SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s;
        """
        result = connectToMySQL(DATABASE_NAME).query_db(query , data)
        ninjas = []
        if result:
            for item in result:
                ninjas.append(cls(item))
        return ninjas

    @classmethod 
    def get_all(cls):
        query = """
            SELECT * FROM ninjas;
        """

        result = connectToMySQL(DATABASE_NAME).query_db(query)
        ninjas = []
        if result:
            for item in result:
                ninjas.append(cls(item))
        return ninjas
    
    @classmethod
    def create_ninja(cls, data):
        query = """
            INSERT INTO ninjas (first_name , last_name , age , dojo_id) VALUES (%(first_name)s ,%(last_name)s , %(age)s , %(dojo_id)s);
        """
        result = connectToMySQL(DATABASE_NAME).query_db(query , data)
        return result