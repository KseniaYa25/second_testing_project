import requests
from tests.configuration import SERVICE_URL

from tests.schemas.get_validate import CreatedDevice


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

