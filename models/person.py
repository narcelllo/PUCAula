from models import Base
from sqlalchemy.orm import mapped_column
from sqlalchemy import INTEGER, CHAR, VARCHAR, DATE


class Person(Base):
    __tablename__ = "person"
    id = mapped_column(INTEGER(), nullable=False, autoincrement=True, primary_key=True)
    cpf = mapped_column(CHAR(11), nullable=False)
    name = mapped_column(VARCHAR(256), nullable=False)
    email = mapped_column(VARCHAR(100), nullable=False)
    phone = mapped_column(VARCHAR(15), nullable=False)
    birth_date = mapped_column(DATE, nullable=False)
