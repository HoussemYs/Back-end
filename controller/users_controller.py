from app import app
from model.users_model import users
from flask import request, make_response
import traceback


obj = users()

@app.route("/users", methods=["GET"])
def get_all_users():
    try:
        return obj.get_all_users()
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in getAll users controller: {e}", 204)

@app.route("/users", methods=["POST"])
def add_user():
    try:
        return obj.add_user(request.form)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in add user controller: {e}", 204)
    
@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    try:
        return obj.get_user(id)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in get user controller: {e}", 204)
    
@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        return obj.update_user(id, request.form)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in update user controller: {e}", 204)
    
@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        return obj.delete_user(id)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in delete user controller: {e}", 204)
    
@app.route("/user/patch/<int:id>", methods=["PATCH"])
def patch_user(id):
    try:
        return obj.patch_user(request.form, id)
    except Exception as e :
        traceback.print_exc()
        return make_response(f"Error in patch user controller : {e}", 204)

@app.route("/users/limit/<int:limit>/page/<int:page>", methods=["GET"])
def limit_user(limit, page):
    try:
        return obj.limit_user(limit, page)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"Error limit user controller : {e}", 204)
    

