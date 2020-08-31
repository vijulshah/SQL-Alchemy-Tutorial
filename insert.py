from sqlalchemy.orm import sessionmaker, relationship
from engine import engine
from modals import *

#Intro: -
# Session maintains a graph of modified models and 
# makes sure the changes are efficiently and 
# consistently flushed to the database when necessary.
# -----------------------------------------------------------------------------------------

#A)- With Session
#Session -> need instance of class to be added

#1-Single inserts
# Session = sessionmaker(bind=engine)
# session = Session()
#1st prod
# products = Products(name="Books",amt=22.10,qty=10)
# session.add(products)
#2nd prod
# products = Products(name="Paints",amt=520,qty=15)
# session.add(products)
#commit added things
# session.commit()
# session.close()

#2 - Bulk inserts
# Session = sessionmaker(bind=engine)
# session = Session()
# products = [
#     Products(name="Bathing Soap",amt=49.99,qty=100),
#     Products(name="Washing Soap",amt=39.56,qty=200)
# ]
# session.bulk_save_objects(products)
# session.commit()
# session.close()

# -----------------------------------------------------------------------------------------

#B) - Without Session
#engine.execute -> takes key value pairs as parameters

# 1-Single insert
products = { "name":"Paper", "amt":50.589, "qty":65 }
engine.execute(Products.__table__.insert(),products)

# 2 - Bulk inserts
products = [
    { "name":"Chocolates", "amt":33.56, "qty":10 },
    { "name":"Face Mask", "amt":100, "qty":30 }
]
engine.execute(Products.__table__.insert(),products)