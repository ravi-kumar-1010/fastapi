from sqlalchemy import Integer, String, Column

from .database import Base


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)


