from pydantic import BaseModel

from typing import List, Optional, Dict, Any


class DeviceData(BaseModel):
    data: Optional[Dict[str, Any]] = None

class Device(BaseModel): 
    id: str
    name: str
    data: DeviceData


class DevicesResponse(BaseModel):
    devices: List[Device] = []



# class DeviceData(BaseModel):
#     color: str
#     capacity: str

# class Device(BaseModel):
#     id: str
#     name: str
#     data: DeviceData


# [{'id': '1', 'name': 'Google Pixel 6 Pro', 'data': {'color': 'Cloudy White', 'capacity': '128 GB'}}, 

#  {'id': '2', 'name': 'Apple iPhone 12 Mini, 256GB, Blue', 'data': None},
#    {'id': '3', 'name': 'Apple iPhone 12 Pro Max', 'data': {'color': 'Cloudy White', 'capacity GB': 512}}, 
#    {'id': '4', 'name': 'Apple iPhone 11, 64GB', 'data': {'price': 389.99, 'color': 'Purple'}}, 
#    {'id': '5', 'name': 'Samsung Galaxy Z Fold2', 'data': {'price': 689.99, 'color': 'Brown'}},
#      {'id': '6', 'name': 'Apple AirPods', 'data': {'generation': '3rd', 'price': 120}},