import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy_xl.decorators import distribute_by_hash
from sqlalchemy_xl import generate_sql


# class MetaDataXL(MetaData):

#     def create_all(self, bind=None, tables=None, checkfirst=True):
#         global DISTRIBUTE_HASH
#         super(MetaDataXL, self).create_all(bind, tables, checkfirst)


# Base = declarative_base(metadata=MetaDataXL())
Base = declarative_base()


@distribute_by_hash('id')
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


@distribute_by_hash('id')
class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.

# engine = create_engine('sqlite:///sqlalchemy_example.db')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.

# Base.metadata.create_all(engine)

print(generate_sql(Base.metadata))
