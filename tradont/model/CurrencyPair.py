from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from tradont.model import Base

class CurrencyPair(Base):
    __tablename__ = 'ccy_pairs'
    id = Column(Integer, Sequence('ccy_pair_id_seq'), primary_key=True)
    symbol_name = Column(String(7), nullable=False)
    base_ccy_id = Column(Integer, ForeignKey('currencies.id'))
    base_ccy = relationship('Currency', foreign_keys=[base_ccy_id])
    quote_ccy_id = Column(Integer, ForeignKey('currencies.id'))
    quote_ccy = relationship('Currency', foreign_keys=[quote_ccy_id])
    pipLocation = Column(Integer, nullable=False)
    displayPrecision = Column(Integer, nullable=False)
    marginRate = Column(DECIMAL(10,5), nullable=False)

