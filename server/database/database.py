from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///flight_booking.db')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)