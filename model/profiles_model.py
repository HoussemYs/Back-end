from app import app
from flask import request, make_response
import psycopg2


class profiles():
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

    def get_all_profiles(self):
        try:
            self.cur.execute("SELECT * FROM profiles")
            self.conn.commit()
            profiles = [
                dict(id=row[0], name=row[1], email=row[2], telephone=row[3], adresse=row[4], image=row[5], description=row[6], user_id=row[7])
                for row in self.cur.fetchall()
            ]
            if profiles is not None:
                res = make_response(profiles, 200)
                # res.headers['Access-Control-Allow-Origin'] = "*"
                return res
            else:
                return make_response({"message":"No profiles found !"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving get all profiles : {e}"}, 500)
        
    def get_profile(self, id):
        try:
            self.cur.execute("SELECT * FROM profiles WHERE id=%s", (id,))
            row = self.cur.fetchone()
            if row is not None:
                profile = dict(id=row[0], name=row[1], email=row[2], telephone=row[3], adresse=row[4], image=row[5], description=row[6], user_id=row[7])
                return make_response(profile, 200)
            else:
                return make_response({"message":"No profile found !"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving get profile : {e}"}, 500)

    def add_profile(self, data):
        try:
            new_name = request.form['name']
            new_email = request.form['email']
            new_telephone = request.form['telephone']
            new_adresse = request.form['adresse']
            new_image = request.form['image']
            new_description = request.form['description']
            new_user_id = request.form['user_id']
            sql = """INSERT INTO profiles (name, email, telephone, adresse, image, description, user_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            self.cur.execute(sql, (new_name, new_email, new_telephone, new_adresse, new_image, new_description, new_user_id))
            self.conn.commit()
            profile_id = self.cur.lastrowid
            return make_response({"message" : f"Profile with the id: {profile_id} created successfully"}, 201)
            # return f"Profile with the id: {profile_id} created successfully", 201
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving add profile : {e}"}, 500)

    def update_profile(self, id, data):
        try:
            current_name = data['name']
            current_email = data['email']
            current_telephone = data['telephone']
            current_adresse = data['adresse']
            current_image = data['image']
            current_description = data['description']
            current_user_id = data['user_id']
            sql = """UPDATE profiles
                    SET username=%s,
                        password=%s,
                        user_id=%s
                    WHERE id=%s"""
            self.cur.execute(sql, (current_name, current_email, current_telephone, 
                                   current_adresse, current_image, current_description,
                                   current_user_id, id))
            self.conn.commit()
            # Return the updated profile
            updated_profile = {
                "name": current_name,
                "email": current_email,
                "telephone": current_telephone,
                "adresse": current_adresse,
                "image": current_image,
                "description": current_description,
                "user_id": current_user_id
            }
            return make_response(updated_profile, 201)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving update profile : {e}"}, 500)
    
    def delete_profile(self, id):
        try:
            self.cur.execute(f"DELETE from profiles WHERE id=%s",(id,) )
            self.conn.commit()
            if self.cur.rowcount>0:
                return make_response("Profile deleted Successfully", 200)
            else:
                return make_response("Nothing Deleted", 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving delete profile : {e}"}, 500)

    def patch_profile(self, data, id):
        try:
            query = "UPDATE profiles SET "
            for key in data:
                query += f"{key}='{data[key]}',"
            query = query[:-1] + f" WHERE id=%s"
            print(query)    
            self.cur.execute(query, (id,) )
            self.conn.commit()
            if self.conn.commit():
            # if self.cur.rowcount>0:
                return make_response({"message":"profile Updated in patch model successfully !"}, 201)
            else:
                return make_response({"message":"Nothing to Updated in patch model"}, 202)
        except Exception as e:
            self.conn.rollback()
            return make_response({"message": f"Error retrieving patch user : {e}"}, 500)
    
    #FILES HEREEEEE
    def profile_upload_image(self, uid, filepath):
        self.cur.execute(f"UPDATE profiles SET image='{filepath}' WHERE id=%s", (uid,) )
        self.conn.commit()
        if self.cur.rowcount>0:
            return make_response({"message":"Profile image updated successfully !"}, 201)
        else:
            return make_response({"message":"Nothing done !!!!!!"}, 202)
        
 