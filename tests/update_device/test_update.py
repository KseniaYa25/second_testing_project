import requests
from tests.configuration import SERVICE_URL
from tests.tools_for_tests import create_device
from tests.schemas.get_validate import UpdatedDevice



def test_update_device_status_code():
    device_data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        },
    }


    device_id = create_device()
    response = requests.put(
        url=SERVICE_URL + f"/{device_id}",
        json=device_data
    )
    
    assert response.status_code == 200




def test_update_device_validation():
    device_data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        },
    }


    device_id = create_device()
    response = requests.put(
        url=SERVICE_URL + f"/{device_id}",
        json=device_data
    )
    

    json_data = response.json()
    validated_response = UpdatedDevice(**json_data)

    print("Новые данные:", validated_response)



#     {
#    "name": "Apple MacBook Pro 16",
#    "data": {
#       "year": 2019,
#       "price": 2049.99,
#       "CPU model": "Intel Core i9",
#       "Hard disk size": "1 TB",
#       "color": "silver"
#    }
# }