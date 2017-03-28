from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Url(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True)
    org_link = Column(String)
    short_link = Column(String, unique=True)
