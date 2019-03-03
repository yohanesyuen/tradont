from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import relationship

class Currency(Base):
    __tablename__ = 'currencies'
    id = Column(Integer, Sequence('currency_id_seq'), primary_key=True)
    name = Column(String(3), nullable=False)

    def __repr__(self):
        return '<Currency(id={}, name={})>'.format(self.id, self.name)
