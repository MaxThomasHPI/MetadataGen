from flask import Flask, url_for


def create_app():
    app = Flask(__name__, static_folder='static')
    #app.config["SERVER_NAME"] = '127.0.0.1:5000'

    #with app.app_context():
        #print(url_for('static', filename='js/main.js'))
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app
