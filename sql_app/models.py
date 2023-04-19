# Importing from SQLAlachemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Import Base from database.py
from .database import Base