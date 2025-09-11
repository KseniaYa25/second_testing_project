import requests
from tests.configuration import SERVICE_URL

from tests.enum.global_enums import GlobalErrorMessages
from tests.tools_for_tests import get_first_device_id

from tests.schemas.get_validate import Device, DevicesResponse
from pydantic import TypeAdapter, ValidationError
from typing import List

def test_get_all_devices():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200
    json_data = response.json()
    try:
        response = DevicesResponse(devices=json_data)
        print(f"✓ Validated {len(response.devices)} devices successfully!")
    
        for device in response.devices:
            print(f"Device ID: {device.id}, Name: {device.name}")
            if device.data:
                print(f"  Data: {device.data}")
            
    except ValidationError as e:
        print(f"Validation failed: {e}")


def test_get_one_device():
    first_device_id = get_first_device_id(SERVICE_URL)
    response = requests.get(url=SERVICE_URL + f"/{first_device_id}")
    assert response.status_code == 200
    try:

        json_data = response.json()
        TypeAdapter(Device).validate_python(json_data)
        
        print(f"Successfully validated with ID: {first_device_id}")
    
    except ValidationError as e:
        print(f"Validation failed: {e}")
        raise AssertionError(f"Validation failed: {e}")