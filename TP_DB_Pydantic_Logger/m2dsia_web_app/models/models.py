from sqlalchemy import Column, String
from database import Base
class User(Base):
    __tablename__ = "users"
# remplissez les paramtres de la classe
# Exemple : email = Column(String(255), primary_key=True, index=True, unique=True,
nullable=False)
.....