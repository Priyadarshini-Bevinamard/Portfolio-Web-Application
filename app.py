import os
from flask import Flask
from controllers.routes import main_blueprint
from models.database import init_db

app = Flask(
    __name__,
    static_folder='frontend',
    static_url_path='/frontend'
)
app.register_blueprint(main_blueprint)
init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
