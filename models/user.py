from models import Base, Person
from sqlalchemy.orm import mapped_column
from sqlalchemy import INTEGER, DATETIME, ForeignKey
from datetime import datetime

class User(Base):
    __tablename__ = "user"
    id = mapped_column(INTEGER(), ForeignKey(Person.id), nullable=False, primary_key=True)
    crate_at = mapped_column(DATETIME, nullable=False, default=datetime.now())
