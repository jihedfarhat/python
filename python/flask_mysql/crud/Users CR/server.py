from flask_app.controllers import users
from flask_app import app

if __name__=="__main__":
    app.run(host='localhost', port=5004, debug=True)
