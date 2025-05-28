from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///restaurant.db', echo=False)

Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
