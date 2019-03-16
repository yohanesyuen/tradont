# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy import DECIMAL
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from tradont.model import Base

class ConversionFactor(Base):
    __tablename__ = 'conversion_factors'
    id = Column(Integer, Sequence('conversion_factors_id_seq'), primary_key=True)
    symbol_id = Column(Integer, ForeignKey('ccy_pairs.id'))
    symbol = relationship('CurrencyPair', foreign_keys=[symbol_id])
    positive_units = Column(DECIMAL(10,5), nullable=False)
    negative_units = Column(DECIMAL(10,5), nullable=False)

