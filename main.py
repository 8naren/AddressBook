from fastapi import FastAPI
from pydantic import BaseModel
from Model import session,Address
from math import sin, cos, sqrt, atan2
global R 
R = 6373.0
app=FastAPI()
class address(BaseModel):
    name : str
    pincode : int
    street_name : str
    lattitude : float
    longitude : float


@app.get("/")
def main():
    """
    First function to give message to find docs in fastapi
    """
    return{
        "message":"http://127.0.0.1:8000/.docs"
    }

@app.post("/add")
def Add_address(data : address):
    """
    To add the Address into the database
    Arguments:
            data : Basemodel
    return:
            dict : message Either added or not

    """
    database_data = session.query(Address).filter(data.lattitude == Address.lattitude and data.longitude == Address.longitude).first()
    if database_data == None:
            address_to_add = Address(name = data.name,pincode = data.pincode,street_name = data.street_name,lattitude = data.lattitude,longitude = data.longitude)
            if address_to_add.Validate(lattitude = data.lattitude, longitude = data.longitude) and address_to_add.isValidPinCode(pincode=str(data.pincode)):
                session.add(address_to_add)
                session.commit()
                return{
                    "message":"added successfully"
                }
            else:
                return{
                    "message":"please check the address pincode must be six digits and did not star with 0 and longitude and lattitude must be in float."
                }
    else:
        return{
            "message":"address already exits"

        }

@app.get("/retrive/address")
def Retrive_distrance(lattitude : float,longitude : float,distance : float):
    """
            Retrive the Addesses based on both lattitude and longitude
            Arguments:
                lattitude: a float
                longitude: a float
            Returns:
                list : Addesses list if the distance is closer to any address in the database

    """
    fetched_data = session.query(Address).all()
    addresses_list=[]
    for each in fetched_data:
        dlat = each.lattitude-lattitude
        dlon = each.longitude-longitude
        a = (sin(dlat/2))**2 + cos(each.lattitude) * cos(lattitude) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = R * c
        if d < distance:
            addresses_list.append({"name":each.name,"pincode":each.pincode,"street_name":each.street_name,"lattitude":each.lattitude,"longitude":each.longitude})
    if len(addresses_list)==0:
            return {
                "message":f"There is no Addresses near to this lattitudes {lattitude} {d} and longitudes {longitude}"}
    return {
        "Near by Addresses":addresses_list
    }
    
@app.put("/update/address")
def update_details(lattitude : float,longitude : float,updated_lattitude : float,updated_longitude : float):
    """
            Update both lattitude and longitude with new values
            Arguments:
                lattitude : a float
                longitude : a float
                updated_lattitude : a float
                updated_longitude : a float

            Returns:
                dict : with message either deleted succesfully or not
    """
    fetched_address = session.query(Address).filter(Address.lattitude == lattitude and Address.longitude == longitude).first()
    if fetched_address == None:
        return{
            "message":f"No address found with this lattitude {lattitude} and longitude {longitude}"
        }
    else:
        fetched_address.lattitude = updated_lattitude
        fetched_address.longitude = updated_longitude
        session.commit()
        return{
            "message":"Address updated successfully"
        }


@app.delete("/delete/address")
def delete_address(lattitude : float,longitude : float):
    """
            To delete the Address in the database by using lattitude and longitude
            Arguments:
                lattitude : a float
                longitude : a float
            Returns:
                dict : with message either deleted succesfully or not
    """
    fetched_address = session.query(Address).filter(Address.lattitude == lattitude,Address.longitude == longitude).first()
    if fetched_address == None:
        return{
            "message":f"No Address found with this lattitude {lattitude} and longitude {longitude}"
        }
    else:
        session.delete(fetched_address)
        session.commit()
        return{
            "message": " Address deleted successfully"
        }

@app.get("/get/address")
def get_address(lattitude : float,longitude : float):
    """
            To get  the Address in the database by using lattitude and longitude
            Arguments:
                lattitude : a float
                longitude : a float
            Returns:
                dict : with required lattitude and longitude or message
    """
    fetched_address = session.query(Address).filter(Address.lattitude == lattitude,Address.longitude == longitude).first()
    if fetched_address==None:
        return{
            "message":f"Address with this lattitude {lattitude} and longitude{longitude} not found."
        }
    else:
        return{
            "address":fetched_address
        }






