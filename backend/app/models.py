from sqlalchemy import Column, Integer, String
from .database import Base

class ImageMetadata(Base):
    __tablename__ = 'image_metadata'

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    size = Column(Integer)
    format = Column(String)