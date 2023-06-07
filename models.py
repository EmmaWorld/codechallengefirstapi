from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Student(Base):
    __tablename__ = 'Student'
    StudentID = Column(Integer, primary_key=True)
    Name = Column(String)
    Email = Column(String)
    Phone = Column(Integer)
    Address = Column(String)
    
    
def create_database():
    engine = create_engine('sqlite:///school_management.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

# Usage:
session = create_database()