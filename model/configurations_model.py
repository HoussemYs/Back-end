from app import app
from flask import request, make_response
import psycopg2
from datetime import datetime


class configurations():
    database = "configsystem"
    user = "postgres"
    password = "houssem"
    host = "localhost"
    port = 5050

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port)
            self.cur = self.conn.cursor()
        except psycopg2.Error as error:
            print(error)
            
            
# configuration_id = self.cur.fetchone()[0]

    
    def get_all_configurations(self):
        try:
            self.cur.execute("SELECT * FROM configurations")
            self.conn.commit()
            configurations = [
                dict(id=row[0], name=row[1], value=row[2], defaultValue=row[3], 
                     createdAt=row[4], createdBy=row[5], updatedBy=row[6], 
                     description=row[7], version=row[8])
                for row in self.cur.fetchall()
            ]
            if configurations is not None:
                res = make_response(configurations, 200)
                # res.headers['Access-Control-Allow-Origin'] = "*"
                return res  
            else:
                return make_response({"message":"No configurations found !"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving get all configurations : {e}"}, 500)
        
    def add_configuration(self, data):
        try:
            new_name = request.form['name']
            new_value = request.form['value']
            # new_defaultValue = request.form['defaultValue']
            new_createdAt = datetime.now()
            new_description = request.form['description']
            new_version = 1
            new_user_id = request.form['user_id']
            # Vérifier si l'utilisateur existe
            self.cur.execute("SELECT id FROM users WHERE id = %s", (new_user_id,))
            user = self.cur.fetchone()
            if not user:
                return "Utilisateur introuvable", 404
            # Récupérer le nom de profil correspondant à l'utilisateur
            self.cur.execute("SELECT name FROM profiles WHERE user_id = %s", (new_user_id,))
            profile = self.cur.fetchone()
            if not profile:
                return "Profil introuvable", 404
            new_createdBy = profile[0]  # Récupérer le nom de l'utilisateur
            sql = """INSERT INTO configurations (name, value, defaultValue, createdAt, createdBy, description, version)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            self.cur.execute(sql, (new_name, new_value, new_value,
                        new_createdAt, new_createdBy, new_description, new_version))
            if self.cur.rowcount == 0:
                # No rows were inserted, so roll back the transaction and raise an exception
                self.conn.rollback()
                raise Exception("Failed to insert row into configurations table")
            self.conn.commit()
            self.cur.execute("SELECT LAST_INSERT_ID();")
            configuration_id = self.cur.fetchone()[0]
            # print(configuration_id) 
            # # Insérer l'entrée correspondante dans la table user_configurations
            # sql = """INSERT INTO user_configurations (user_id, configuration_id)
            #     VALUES (%s, %s)"""
            # self.cur.execute(sql, (user, configuration_id))
            # self.conn.commit()
            return f"Configuration with the id: {configuration_id} created with successfully", 201
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving add profile : {e}"}, 500)

    def delete_configuration(self, id):
        try:
            self.cur.execute(f"DELETE from configurations WHERE id=%s",(id,) )
            self.conn.commit()
            if self.cur.rowcount>0:
                return make_response("Configuration deleted Successfully", 200)
            else:
                return make_response("Nothing Deleted", 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving delete configuration : {e}"}, 500)
