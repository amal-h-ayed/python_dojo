from flask_app.config.mysqlconnection import DB , connectToMySQL

class User:
    def __init__(self,data) :
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "select * from users"
        results = connectToMySQL(DB).query_db(query)
        if results == [] :
            return []
        users = []
        for user in results:
            users.append(cls(user))
        return users
    @classmethod
    def create(cls,data):
        query ="insert into users (first_name,last_name,email) values(%(first_name)s,%(last_name)s,%(email)s)"
        results = connectToMySQL(DB).query_db(query,data)
        return results