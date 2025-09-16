import requests
from tests.configuration import SERVICE_URL

from tests.schemas.get_validate import CreatedDevice
from tests.generators.device import DeviceBuilder


def test_create_device_status_code():
    device_data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        },
    }

    response = requests.post(
        url=SERVICE_URL,
        json=device_data
    )
    
    assert response.status_code == 200

def test_create_device_validation():
    builder = DeviceBuilder() 
    random_device = (builder
                     .reset()
                     .with_name()
                     .with_year()
                     .with_price()
                     .with_cpu()
                     .with_disk_size()
                     .with_color()
                     .build())
    
    response = requests.post(
        url=SERVICE_URL,
        json=random_device
    )
    
    json_data = response.json()
    validated_response = CreatedDevice(**json_data)
    print("Полученные данные:", validated_response)


def test_create_device_wihout_price_field():
    builder = DeviceBuilder() 
    random_device = (builder
                     .reset()
                     .with_name()
                     .with_year()
                     .with_cpu()
                     .with_disk_size()
                     .with_color()
                     .build())
    
    response = requests.post(
        url=SERVICE_URL,
        json=random_device
    )
    
    json_data = response.json()
    validated_response = CreatedDevice(**json_data)
    print("Полученные данные:", validated_response)
# {
#    "name": "Apple MacBook Pro 16",
#    "data": {
#       "year": 2019,
#       "price": 1849.99,
#       "CPU model": "Intel Core i9",
#       "Hard disk size": "1 TB"
#    }
# }

