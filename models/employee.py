from models import Base, Person
from sqlalchemy.orm import mapped_column
from sqlalchemy import INTEGER, DATE, VARCHAR, NUMERIC, ForeignKey


class Employee(Base):
    __tablename__ = "employee"
    id = mapped_column(INTEGER(), ForeignKey(Person.id), nullable=False, primary_key=True)
    admission_date = mapped_column(DATE(), nullable=False)
    salary = mapped_column(NUMERIC(8.2), nullable=False)
    bank_code = mapped_column(VARCHAR(4), nullable=False)
    bank_agency = mapped_column(VARCHAR(10), nullable=False)
    bank_number = mapped_column(VARCHAR(15), nullable=False)
