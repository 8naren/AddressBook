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
    return{
        "message":"http://127.0.0.1:8000/.docs"
    }

@app.post("/add")
def Add_address(data : address):
    database_data = session.query(Address).filter(data.lattitude == Address.lattitude and data.longitude == Address.longitude).first()
    if database_data == None:
            address_to_add = Address(name = data.name,pincode = data.pincode,street_name = data.street_name,lattitude = data.lattitude,longitude = data.longitude)
            if address_to_add.validate(lattitude = data.lattitude, longitude = data.longitude):
                session.add(address_to_add)
                session.commit()
                return{
                    "message":"added successfully"
                }
            else:
                return{
                    "message":"please check the address"
                }
    else:
        return{
            "message":"address already exits"

        }

@app.get("/retrive/address")
def Retrive_distrance(lattitude : float,longitude : float,distance:float):
    fetched_data = session.query(Address).all()
    addresses_list=[]
    for each in fetched_data:
        dlat = each.lattitude-lattitude
        dlon = each.longitude-longitude
        a = (sin(dlat/2))**2 + cos(each.lattitude) * cos(lattitude) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = R * c
        if d < distance:
            addresses_list.append(each.__repr__())
    if len(addresses_list)==0:
            return {"di":d}
    return {
        "near by addresses":addresses_list
    }
    

# @app.get('/data')
# def get_alldata():
#     f = session.query(Address).all()
#     for i in f:
#         print(i.lat,i.lon)


@app.put("/update/address")
def update_details(lattitude : float,longitude : float,update_address : address):
    fetched_address = session.query(Address).filter(Address.lattitude == lattitude and Address.longitude == longitude).first()
    if fetched_address == None:
        return{
            "message":f"No address found with this lattitude {lattitude} and longitude {longitude}"
        }
    else:
        pass


@app.delete("/delete/address")
def delete_address(lattitude : float,longitude : float):
    fetched_address = session.query(Address).filter(Address.lattitude == lattitude,Address.longitude == longitude).first()
    if fetched_address == None:
        return{
            "message":f"No address found with this lattitude {lattitude} and longitude {longitude}"
        }
    else:
        pass






