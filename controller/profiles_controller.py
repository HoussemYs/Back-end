from app import app
from model.profiles_model import profiles
from flask import request, make_response, send_file
import traceback
from datetime import datetime


obj = profiles()

@app.route("/profiles", methods=["GET"])
def get_all_profiles():
    try:
        return obj.get_all_profiles()
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in getAll profiles controller: {e}", 204)

@app.route("/profiles", methods=["POST"])
def add_profile():
    try:
        return obj.add_profile(request.form)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in add profile controller: {e}", 204)
    
@app.route("/profile/<int:id>", methods=["GET"])
def get_profile(id):
    try:
        return obj.get_profile(id)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in get profile controller: {e}", 204)
    
@app.route("/profile/<int:id>", methods=["PUT"])
def update_profile(id):
    try:
        return obj.update_profile(id, request.form)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in update profile controller: {e}", 204)
    
@app.route("/profile/<int:id>", methods=["DELETE"])
def delete_profile(id):
    try:
        return obj.delete_profile(id)
    except Exception as e:
        traceback.print_exc()
        return make_response(f"error in delete profile controller: {e}", 204)

@app.route("/profile/patch/<int:id>", methods=["PATCH"])
def patch_profile(id):
    try:
        return obj.patch_profile(request.form, id)
    except Exception as e :
        traceback.print_exc()
        return make_response(f"Error in patch profile controller : {e}", 204)
 
@app.route("/profile/<uid>/upload/image", methods=["PUT"])
def profile_upload_image(uid):
    file = request.files['image']
    # file.save(f"uploads/{file.filename}")
    uniqueFileName = str(datetime.now().timestamp()).replace(".", "")
    fileNameSplit = file.filename.split(".")
    ext = fileNameSplit[len(fileNameSplit)-1]
    finalFilePath = f"uploads/{uniqueFileName}.{ext}"
    file.save(finalFilePath)
    return obj.profile_upload_image(uid, finalFilePath)

@app.route("/uploads/<filename>")
def profile_get_image(filename):
    return send_file(f"uploads/{filename}")