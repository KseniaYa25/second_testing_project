import requests
from tests.configuration import SERVICE_URL


def get_first_device_id(SERVICE_URL):
    response = requests.get(url=SERVICE_URL)
    response.raise_for_status()  # Проверка HTTP статуса
    json_data = response.json()
    if not json_data:
        raise ValueError("Response is empty or None")
    print(json_data[0])
    return json_data[0]['id']  # Изменено с 'device_id' на 'id'