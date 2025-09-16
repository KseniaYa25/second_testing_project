import requests
from tests.configuration import SERVICE_URL
from tests.tools_for_tests import create_device
from tests.schemas.get_validate import UpdatedDevice
from pydantic import TypeAdapter
from tests.generators.device import DeviceBuilder



def test_update_device_validation():
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


    device_id = create_device()
    response = requests.put(
        url=SERVICE_URL + f"/{device_id}",
        json=random_device
    )
    

    json_data = response.json()
    validated_response = UpdatedDevice(**json_data)

    assert response.status_code == 200

    print("Новые данные:", validated_response)



# {
#    "name": "Apple MacBook Pro 16 (Updated Name)"
# }
def test_patch_device():
    builder = DeviceBuilder()
    created_device_data = create_device()
    get_response = requests.get(url=f"{SERVICE_URL}/{created_device_data}")
    if get_response.status_code == 200:
        original_device = get_response.json()
        original_name = original_device["name"]

        print(f"Имя созданного устройства: {original_name}")
    else:
        print(f"Ошибка получения устройства: {get_response.status_code}")
        print(f"Ответ сервера: {get_response.text}")
        return
    

    patch_data = {
        "name": builder.with_name().build()["name"]
    }

    response = requests.patch(
        url=f"{SERVICE_URL}/{created_device_data}",
        json=patch_data,
    )


    json_data = response.json()
    validated_response = TypeAdapter(UpdatedDevice).validate_python(json_data)
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