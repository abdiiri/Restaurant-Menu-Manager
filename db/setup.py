from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Base class for all models
Base = declarative_base()

# Create a persistent SQLite database file named 'restaurant.db'
engine = create_engine('sqlite:///restaurant.db', echo=False)

# Create a session factory
Session = sessionmaker(bind=engine)

# Initialize the database (creates tables if they don't exist)
def init_db():
    Base.metadata.create_all(engine)
