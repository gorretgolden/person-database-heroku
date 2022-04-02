import connexion
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

# # Create the Connexion application instance
# app = connexion.App(__name__, specification_dir="./")

# # Read the swagger.yml file to configure the endpoints
# app.add_api('swagger.yml')

# # Get the underlying Flask app instance
# application = app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

@app.route('/home')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return jsonify({'yes':'yes'})




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)