import os
from flask import Flask


def create_app(config_name='default'):
    app = Flask(__name__, template_folder='../templates')

    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB
    app.config['UPLOAD_FOLDER'] = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 'uploads')
    app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'docx'}
    app.config['TESTING'] = (config_name == 'testing')

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    from app.routes import main
    app.register_blueprint(main)

    return app