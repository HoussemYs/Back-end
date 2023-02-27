from app import app

@app.route("/login")
def login():
    return ("this is login page")
