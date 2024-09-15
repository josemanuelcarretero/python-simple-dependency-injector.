services = {
    "my_singleton_service": {
        "class": "tests/services/my_module.py#MyService",
        "scope": "singleton",
    },
    "my_service": {
        "class": "tests/services/my_module.py#MyService",
    },
    "my_factory_service": {
        "factory": {
            "class": "tests/services/my_module.py#MyFactory",
            "method": "create_service",
        },
        "scope": "request",
    },
    "my_instance_service": {
        "instance": "tests/services/my_module.py#MyInstance",
    },
}

imports = [{"resource": "another_services.py"}]