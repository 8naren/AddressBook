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

@app.get("/retrive/{lattitude}")
def Retrive_distrance(lattitude : float,longitude : float,distance:float):
    d = session.query(Address).all()
    l=[]
    for i in d:
        dlat = i.lattitude-lattitude
        dlon = i.longitude-longitude
        a = (sin(dlat/2))**2 + cos(i.lattitude) * cos(lattitude) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = R * c
        if d < distance:
            l.append(i.__repr__())
    if len(l)==0:
            return {"di":d}
    return {
        "near by addresses":l
    }
    

# @app.get('/data')
# def get_alldata():
#     f = session.query(Address).all()
#     for i in f:
#         print(i.lat,i.lon)


# @app.put("/update{lat}{lon}")
# def update_details(name:str,address:str):
#     db_user = session.query(Details).filter(Details.Name==name).first()
#     if db_user == None:
#         return{
#             "message":f"No details available with this username {name}"
#         }



