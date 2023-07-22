from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# create a sqlite engine instance
# DATABASE_URI = "postgresql+psycopg2://postgres:postgres@192.168.1.103:5432/test"
DATABASE_URI = os.environ.get('DATABASE_URL')
engine = create_engine(DATABASE_URI)

# create a DeclarativeMeta instance
Base = declarative_base()

# ceate SessionLocal class from sessionmaker factory
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
