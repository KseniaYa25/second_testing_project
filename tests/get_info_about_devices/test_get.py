import requests
from tests.configuration import SERVICE_URL

from tests.enum.global_enums import GlobalErrorMessages
from tests.tools_for_tests import get_first_device_id

from tests.schemas.get_validate import Device
from pydantic import TypeAdapter

def test_get_all_devices_successfully():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200


def test_get_all_devices_list_validation():
    response = requests.get(url=SERVICE_URL)
    json_data = response.json()
    TypeAdapter(Device).validate_python(json_data[0])


def test_get_one_device_status_code():
    first_device_id = get_first_device_id(SERVICE_URL)
    response = requests.get(url=SERVICE_URL + f"/{first_device_id}")
    assert response.status_code == 200


def test_get_one_device_validation():
    first_device_id = get_first_device_id(SERVICE_URL)
    response = requests.get(url=SERVICE_URL + f"/{first_device_id}")
    json_data = response.json()
    TypeAdapter(Device).validate_python(json_data)

def test_get_several_obj_by_ids(several_ids):
    ids = several_ids
    id1, id2, id3 = ids
    response =requests.get(f"https://api.restful-api.dev/objects?id={id1}&id={id2}&id={id3}")
    json_data = response.json()
    for device in json_data:
        TypeAdapter(Device).validate_python(device)
        print(f"Successfully validated with ID: {device['id']}")

def test_get_several_obj_by_ids_status_code(several_ids):
    ids = several_ids
    id1, id2, id3 = ids
    response =requests.get(f"https://api.restful-api.dev/objects?id={id1}&id={id2}&id={id3}")
    assert response.status_code == 200