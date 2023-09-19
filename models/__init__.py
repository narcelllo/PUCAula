from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session 



HOST = "localhost"
DATABASE = "library"
USERNAME = "root"
PASSWORD = "root"
PORT = "3306"

#instance = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
instance = "sqlite:///library"

if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autocommit=False)

from models.base import Base
from models.person import Person
from models.employee import Employee
from models.user import User