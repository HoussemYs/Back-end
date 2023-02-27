from app import app
from flask import request, make_response
import psycopg2


class users():
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

    def get_all_users(self):
        try:
            self.cur.execute("SELECT * FROM users")
            self.conn.commit()
            users = [
                dict(id=row[0], username=row[1], password=row[2], type_id=row[3])
                for row in self.cur.fetchall()
            ]
            if users is not None:
                return make_response(users, 200)
            else:
                return make_response({"message":"No users found !"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving get all users : {e}"}, 500)
        
    def get_user(self, id):
        try:
            self.cur.execute("SELECT * FROM users WHERE id=%s", (id,))
            row = self.cur.fetchone()
            if row is not None:
                user = dict(id=row[0], username=row[1], password=row[2], type_id=row[3])
                return make_response(user, 200)
            else:
                return make_response({"message":"No user found !"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving get user : {e}"}, 500)

    def add_user(self, data):
        try:
            # if 'username' not in data or 'password' not in data or 'type_id' not in data:
            #     return "Missing required parameters ", 400
            new_username = request.form['username']
            new_password = request.form['password']
            new_type_id = request.form['type_id']
            sql = """INSERT INTO users (username, password, type_id)
                    VALUES (%s, %s, %s)"""
            self.cur.execute(sql, (new_username, new_password, new_type_id))
            self.conn.commit()
            user_id = self.cur.lastrowid
            return make_response({"message" : f"User with the id: {user_id} created successfully"}, 201)
            # return f"User with the id: {user_id} created successfully", 201
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving add user : {e}"}, 500)

    def update_user(self, id, data):
        try:
            current_username = data['username']
            current_password = data['password']
            current_type_id = data['type_id']
            sql = """UPDATE users
                    SET username=%s,
                        password=%s,
                        type_id=%s
                    WHERE id=%s"""
            self.cur.execute(sql, (current_username, current_password, current_type_id, id))
            self.conn.commit()
            # Return the updated user
            updated_user = {
                "username": current_username,
                "password": current_password,
                "type_id": current_type_id
            }
            return make_response(updated_user, 201)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving update user : {e}"}, 500)
    
    def delete_user(self, id):
        try:
            self.cur.execute(f"DELETE from users WHERE id=%s",(id,) )
            self.conn.commit()
            if self.cur.rowcount>0:
                return make_response("User deleted Successfully", 200)
            else:
                return make_response("Nothing Deleted", 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving delete user : {e}"}, 500)

    def patch_user(self, data, id):
        #UPDATE users SET col=val, col=val WHERE id={id}
        try:
            sql_query = "UPDATE users SET "
            for key in data:
                sql_query += f"{key}='{data[key]}',"
            sql_query = sql_query[:-1] + f" WHERE id=%s"
            print(sql_query)    
            self.cur.execute(sql_query, (id,) )
            self.conn.commit()
            if self.cur.rowcount>0:
                return make_response({"message":"User Updated in patch model successfully !"}, 201)
            else:
                return make_response({"message":"Nothing to Updated in patch model"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving patch user : {e}"}, 500)
        
    def limit_user(self, limit, page):
        limit = int (limit)
        page = int (page)
        start = (page - 1 ) * limit
        sql_query = f"SELECT * FROM users LIMIT {start} OFFSET {limit}"
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        if len(result)>0:
            result = make_response({"payload":result, "page number": page, "limit": limit}, 200)
            # result.headers['Acces-Control-Allow-Origin']= "*"
            return result
        else:
            return make_response({"message":"No Data Found!"}, 204)