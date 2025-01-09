from dataclasses import dataclass

import heisskleber

import babbelfish


def test_create_from_dict() -> None:
    input_dict = {
        "name": "test",
        "output": {
            "mqtt": {
                "host": "mqtt.example.com",
                "port": 1883,
            },
            "zmq": {
                "host": "localhost",
                "port": 5555,
            },
        },
        "input": {"udp": {"host": "localhost", "port": 6969}},
    }

    test_dict = babbelfish.ServiceConf.from_dict(input_dict)

    assert isinstance(test_dict.senders["mqtt"], heisskleber.MqttSender)
    assert isinstance(test_dict.senders["zmq"], heisskleber.ZmqSender)
    assert isinstance(test_dict.receivers["udp"], heisskleber.UdpReceiver)


def test_simple_inheritance() -> None:
    @dataclass
    class TestConf(babbelfish.ServiceConf):
        testing: bool = False

    input_dict = {
        "name": "test",
        "testing": True,
        "output": {
            "mqtt": {
                "host": "mqtt.example.com",
                "port": 1883,
            },
            "zmq": {
                "host": "localhost",
                "port": 5555,
            },
        },
        "input": {"udp": {"host": "localhost", "port": 6969}},
    }

    test_dict = TestConf.from_dict(input_dict)

    assert test_dict.testing is True
    assert isinstance(test_dict.senders["mqtt"], heisskleber.MqttSender)
    assert test_dict.senders["mqtt"].config.host == "mqtt.example.com"
