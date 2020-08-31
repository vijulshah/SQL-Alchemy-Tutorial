from sqlalchemy import create_engine
import secrets

connUrl = "mysql://{0}:{1}@{2}/{3}".format(secrets.dbuser, secrets.dbpassword, secrets.dbhost, secrets.dbname)
engine = create_engine(connUrl, echo = True)
# engine is nothing, but a connection object to our DB

# ----------------------------------------------------------------
# How To Start Project in VS Code : 
# ----------------------------------------------------------------
# source venv/bin/activate
# virtualenv venv
# To run a file : python filename.py