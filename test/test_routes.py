from flask import Flask
from routes.contacts import contacts
#from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from models.contacts import Contact

import pytest
import flask_sqlalchemy

@pytest.fixture
def client(mocker):
    app = Flask(__name__)
    app.register_blueprint(contacts)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    flask_sqlalchemy.SQLAlchemy(app)

    mocker.patch("flask_sqlalchemy.SQLAlchemy.init_app", return_value=True)
    mocker.patch("flask_sqlalchemy.SQLAlchemy.create_all", return_value=True)
    mocker.patch('flask_sqlalchemy._QueryProperty.__get__')

    client = app.test_client()

    return client

def test_base_route(client):
    response = client.get('/')
    assert response.status_code == 200
    #print(response)