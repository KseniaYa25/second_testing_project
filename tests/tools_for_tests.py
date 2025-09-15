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