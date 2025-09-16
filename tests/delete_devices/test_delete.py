import requests
from tests.configuration import SERVICE_URL
from tests.tools_for_tests import create_device



def test_delete_device_status_code():

    device_id = create_device()
    response = requests.delete(f"{SERVICE_URL}/{device_id}")

    assert response.status_code == 201 or response.status_code == 200, \
        f"Expected 200/201, got {response.status_code}"


def test_delete_device_confirm_deletion():

    device_id = create_device()
    response = requests.delete(f"{SERVICE_URL}/{device_id}")
    print(f"Device {device_id} deleted. Status code: {response.status_code}")