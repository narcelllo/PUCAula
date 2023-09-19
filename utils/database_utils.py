from models import *


def create_tables():
    Base.metadata.create_all(bind=engine)