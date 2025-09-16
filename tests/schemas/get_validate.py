from pydantic import BaseModel

from typing import List, Optional, Dict, Any


class Device(BaseModel): 
    id: str
    name: str
    data: Optional[Dict[str, Any]] = None


class DevicesResponse(BaseModel):
    devices: List[Device] = []


class CreatedDevice(BaseModel):
    id: str
    name: str
    data: Optional[Dict[str, Any]] = None
    createdAt: str

class UpdatedDevice(BaseModel):
    id: str
    name: str
    data: Optional[Dict[str, Any]] = None
    updatedAt: str

# {
#    "id": "7",
#    "name": "Apple MacBook Pro 16",
#    "data": {
#       "year": 2019,
#       "price": 1849.99,
#       "CPU model": "Intel Core i9",
#       "Hard disk size": "1 TB"
#    },
#    "createdAt": "2022-11-21T20:06:23.986Z"
# }


# [{'id': '1', 'name': 'Google Pixel 6 Pro', 'data': {'color': 'Cloudy White', 'capacity': '128 GB'}}, 

#  {'id': '2', 'name': 'Apple iPhone 12 Mini, 256GB, Blue', 'data': None},
#    {'id': '3', 'name': 'Apple iPhone 12 Pro Max', 'data': {'color': 'Cloudy White', 'capacity GB': 512}}, 
#    {'id': '4', 'name': 'Apple iPhone 11, 64GB', 'data': {'price': 389.99, 'color': 'Purple'}}, 
#    {'id': '5', 'name': 'Samsung Galaxy Z Fold2', 'data': {'price': 689.99, 'color': 'Brown'}},
#      {'id': '6', 'name': 'Apple AirPods', 'data': {'generation': '3rd', 'price': 120}},