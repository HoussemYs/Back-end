from flask import Flask

app = Flask(__name__)

# import controller.login_controller as login_controller

from controller import *

# if __name__ == '__main__':
#     app.run(debug=True)