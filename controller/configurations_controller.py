from app import app
from model.configurations_model import configurations
from flask import request, make_response, send_file
import traceback
from datetime import datetime

obj = configurations()

@app.route("/configurations", methods=["GET"])
def get_all_configurations():
    try:
        return obj.get_all_configurations()
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in getAll configurations controller: {e}", 204)

@app.route("/configurations", methods=["POST"])
def add_configuration():
    try:
        return obj.add_configuration(request.form)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in add configuration controller: {e}", 204)
    
@app.route("/configuration/<int:id>", methods=["DELETE"])
def delete_configuration(id):
    try:
        return obj.delete_configuration(id)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in delete configuration controller: {e}", 204)
