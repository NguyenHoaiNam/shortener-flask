# -*- coding: utf8 -*-
import config

from sqlalchemy import create_engine
from app.models import Base

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)

if __name__ == '__main__':
    # Create a table with three columns as Url class
    Base.metadata.create_all(engine)
