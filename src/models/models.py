from sqlalchemy import Column, Integer, String
from src.database.database import Base


# define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
