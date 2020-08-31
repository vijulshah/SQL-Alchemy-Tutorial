from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from engine import engine

# declarative base is used to map class with DB table
Base = declarative_base()

# sqlalchemy will automatically set AUTO_INCREMENT 
class Products(Base):
    __tablename__ = "products"

    id = Column('id', Integer, primary_key = True, autoincrement = True)
    name = Column('name', String(20))
    amt = Column('amt', Float)
    qty = Column('qty', Integer)

class Customers(Base):
    __tablename__ = "customers"

    id = Column('id', Integer, primary_key = True, autoincrement = False)
    name = Column('name', String(20))

#create all tables
# Base.metadata.create_all(bind=engine)
#checkfirst=True

#create selected tables
table_objects = [Customers.__table__]
Base.metadata.create_all(bind=engine,tables=table_objects)
checkfirst=True