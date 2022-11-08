from sqlalchemy import create_engine,Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.future import Engine
import sqlalchemy
import re

engine:Engine = create_engine("sqlite:///./details.db")
Base = declarative_base()
session = Session(bind=engine)

metadata=sqlalchemy.MetaData()

class Address(Base):
    """
    A class to represent a Address.

    ...

    Attributes
    ----------
    name : str
        name name of the person
    pincode : int
        pincode of the address
    street_name : str
        street name of the address
    lattitude : float
        lattitude of the address
    longitude : float
        longitude of the address

    Methods
    -------
    Validate(lattitude,longitude):
        validates the Address.
    """
    __tablename__ = "AddressBook"
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    pincode = Column(Integer)
    street_name = Column(String(100))
    lattitude = Column(Float)
    longitude = Column(Float)

    def Validate(self,lattitude,longitude):
        """
            Validates both lattitude and longitude
            Arguments:
                lattitude: a float
                longitude: a float
            Returns:
                True : if Condition Satisfies
                False : if Condition fails
        """
        if (lattitude >= -90 and lattitude <= 90) and (longitude >= -180 and longitude <= 180):
            return True
        else:
            return False

    def isValidPinCode(self,pincode):
        regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
        p = re.compile(regex)
        if re.match(p,pincode):
            return True
        else:
            return False


# To drop the entire table
# Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine) # To create table