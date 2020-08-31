from sqlalchemy import select
from sqlalchemy.orm import sessionmaker, relationship
from engine import engine
from modals import *

#A)- With Session

#1st - show all products
# Session = sessionmaker(bind=engine)
# session = Session()
# products_result = session.query(Products).all()
# for prod in products_result:
#     print(prod.id, prod.name, prod.amt, prod.qty)
# session.commit()
# session.close()

#2nd - show products with condition
# Session = sessionmaker(bind=engine)
# session = Session()
# products_result = session.query(Products).filter(Products.amt > 50)
# for prod in products_result:
#     print(prod.id, prod.name, prod.amt, prod.qty)
# session.commit()
# session.close()

# -----------------------------------------------------------------------------------------

# B) - Without Session

# 1st - show all products
products_query = select([Products])
products_result = engine.execute(products_query)
for prod in products_result:
    print(prod.id, prod.name, prod.amt, prod.qty)

# 2nd - show products with condition
products_query = select([Products.id, Products.amt]).where(Products.qty > 50)
products_result = engine.execute(products_query)
for prod in products_result:
    print(prod.id, prod.amt)

# filter example query
# query(names).join(grad_year).filter(year=1999).filter(last_name="Shah")