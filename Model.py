from sqlalchemy import create_engine,Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.future import Engine
import sqlalchemy

engine:Engine = create_engine("sqlite:///./details.db")
Base = declarative_base()
session = Session(bind=engine)

metadata=sqlalchemy.MetaData()

class Address(Base):
    __tablename__ = "AddressBook"
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    pincode = Column(Integer)
    street_name = Column(String(100))
    lattitude = Column(Float)
    longitude = Column(Float)

    def validate(self,lattitude,longitude):
        if (lattitude >= -90 and lattitude <= 90) and (longitude >= -180 and longitude <= 180):
            return True
        else:
            return False

    def __repr__(self):
        return {"name":self.name,"pincode":self.pincode,"street":self.street_name,"lattitude":self.lattitude,"longitude":self.longitude}

# "-90<=X<=+90 and -180<=Y<=180."

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)