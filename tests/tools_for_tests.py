import requests
from tests.configuration import SERVICE_URL


def get_first_device_id(SERVICE_URL):
    response = requests.get(url=SERVICE_URL)
    response.raise_for_status()  
    json_data = response.json()
    if not json_data:
        raise ValueError("Response is empty or None")
    return json_data[0]['id']  


def get_ids():
    if True:
        json_data = requests.get(url=SERVICE_URL).json()
        id_list = []
        counter = 0
        for item in json_data:
            id = item.get('id')
            print(id)
            id_list.append(id)
            counter += 1
            if counter == 3:
                break
    print (id_list)
    return id_list

get_ids()



def create_device():
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
    
    json_response = response.json()
    device_id = json_response.get('id')

    print(f"Booking created with id: {device_id}")
    return device_id