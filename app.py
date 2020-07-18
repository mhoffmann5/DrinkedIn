from flask import Flask
from app1.routes.Home import home_page
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.register_blueprint(home_page)

bootstrap = Bootstrap(app)

if __name__ == '__main__':
    app.run()
