from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

@app.route("/", methods=['GET'])
def getFunction():
    return jsonify( [
                        {
                            'message': 'HTTP method \'GET\' was called!'
                        }
                    ]
                )

if __name__ == '__main__':
    app.run(debug=True)