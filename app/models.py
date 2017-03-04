from app.views import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    org_link = db.Column(db.String(250), unique=True)
    short_link = db.Column(db.String(100), unique=True)
