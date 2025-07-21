from sqlalchemy import Column, Integer, String
from database import Base

class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    note_text = Column(String, nullable=False)
    title = Column(String, nullable=False)

