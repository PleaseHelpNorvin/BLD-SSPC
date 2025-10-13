from flask import Flask
from app.routes import register_routes
import os

# Set template folder relative to this file
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
