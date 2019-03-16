from sqlalchemy import create_engine
from tradont.common import config

config = config.Config()
config.load()

config = config.db_config

protocol = 'mysql'
user = config['username']
password = config['password']

host = config['hostname']
database = config['database']
url = '{}://{}:{}@{}/{}'.format(protocol, user, password, host, database)
#engine = create_engine(url, echo=True)
engine = create_engine(url, echo=False)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

from tradont.model.Currency import Currency
from tradont.model.CurrencyPair import CurrencyPair
from tradont.model.ConversionFactor import ConversionFactor

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

__all__ = [
        'Base',
        'Currency',
        'CurrencyPair',
        'ConversionFactor',
        'Session']

