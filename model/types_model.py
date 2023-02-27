from app import app
from flask import request, make_response
import psycopg2


class types():
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

    def get_all_types(self):
        try:
            self.cur.execute("SELECT * FROM types")
            self.conn.commit()
            types = [
                dict(id=row[0], name=row[1], description=row[2])
                for row in self.cur.fetchall()
            ]
            if types is not None:
                return make_response(types, 200)
                # return make_response({"type":types}, 200)
                # return jsonify(types) ## Content-Type : application.jsonify
                # return {"payload" : types} ## Content-Type : application.json
                # return json.dumps(types) ## Content-Type : Text.html
            else:
                return make_response({"message":"No types found !"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving get all types : {e}"}, 500)
        
    def get_type(self, id):
        try:
            self.cur.execute("SELECT * FROM types WHERE id=%s", (id,))
            row = self.cur.fetchone()
            if row is not None:
                type = dict(id=row[0], name=row[1], description=row[2])
                # return jsonify(type)
                return make_response(type, 200)
            else:
                return make_response({"message":"No type found !"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving get type : {e}"}, 500)
        
    def add_type(self, data):
        try:
            # if 'name' not in data or 'description' not in data:
            #     return "Missing required parameters 'name' or 'description'", 400
            new_name = request.form['name']
            new_description = request.form['description']
            sql = """INSERT INTO types (name, description)
                    VALUES (%s, %s)"""
            self.cur.execute(sql, (new_name, new_description))
            self.conn.commit()
            type_id = self.cur.lastrowid
            return make_response({"message" : f"Type with the id: {type_id} created successfully"}, 201)
            # return f"Type with the id: {type_id} created successfully", 201
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving add type : {e}"}, 500)

    def update_type(self, id, data):
        try:
            current_name = data['name']
            current_description = data['description']

            sql = """UPDATE types
                    SET name=%s,
                        description=%s
                    WHERE id=%s"""
            self.cur.execute(sql, (current_name, current_description, id))
            self.conn.commit()

            # Return the updated type
            updated_type = {
                "name": current_name,
                "description": current_description
            }
            return make_response(updated_type, 201)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving update type : {e}"}, 500)
            
    def delete_type(self, id):
        try:
            self.cur.execute(f"DELETE from types WHERE id=%s",(id,) )
            self.conn.commit()
            if self.cur.rowcount>0:
                return make_response("Type deleted Successfully", 200)
            else:
                return make_response("Nothing Deleted", 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving delete type : {e}"}, 500)
        
    def patch_type(self, data, id):
        try:
            query = "UPDATE types SET "
            for key in data:
                query += f"{key}='{data[key]}',"
            query = query[:-1] + f" WHERE id=%s"
            print(query)    
            self.cur.execute(query, (id,) )
            self.conn.commit()
            if self.cur.rowcount>0:
                return make_response({"message":"Type Updated in patch model successfully !"}, 201)
            else:
                return make_response({"message":"Nothing to Updated in patch model"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving patch user : {e}"}, 500)