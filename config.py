from flask_restful import fields
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


engine = create_engine("mysql+pymysql://root:@localhost:3306/passportRG")
if not database_exists(engine.url):
    create_database(engine.url)
Secretkey = 'ThisIsAReallyHardToGuessSecret!'
resource_fields = {
    'Country': fields.String,
    'Name': fields.String,
    'Surname': fields.String,
    'Sex': fields.String,
    'DateOfBirth': fields.Integer,
    'Nationality': fields.String,
    'ExpirationDate': fields.Integer,
    'Number': fields.String,
    'Status': fields.Boolean,
    'Problem': fields.String
}


