from app import app
from model.types_model import types
from flask import request, make_response
import traceback


obj = types()

@app.route("/types", methods=["GET"])
def get_all_types():
    try:
        return obj.get_all_types()
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in getAll types controller: {e}", 204)

@app.route("/types", methods=["POST"])
def add_type():
    try:
        return obj.add_type(request.form)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in add type controller: {e}", 204)
    
@app.route("/type/<int:id>", methods=["GET"])
def get_type(id):
    try:
        return obj.get_type(id)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in get type controller: {e}", 204)
    
@app.route("/type/<int:id>", methods=["PUT"])
def update_type(id):
    try:
        return obj.update_type(id, request.form)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in update type controller: {e}", 204)
    
@app.route("/type/<int:id>", methods=["DELETE"])
def delete_type(id):
    try:
        return obj.delete_type(id)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in delete type controller: {e}", 204)
    
@app.route("/type/patch/<int:id>", methods=["PATCH"])
def patch_type(id):
    try:
        return obj.patch_type(request.form, id)
    except Exception as e :
        traceback.print_exc()
        return make_response(f"Error in patch type controller : {e}", 204)

