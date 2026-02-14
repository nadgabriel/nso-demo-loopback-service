import pytest

def test_loopback_data_structure():
    service_data = {
        "device": "ios1",
        "id": 100,
        "ip_address": "10.10.10.1"
    }

    assert service_data["id"] == 100
    assert service_data["ip_address"].count(".") == 3
