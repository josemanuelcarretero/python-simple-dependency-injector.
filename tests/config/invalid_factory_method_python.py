services = {
    "invalid_factory_method": {
        "factory": {
            "class": "tests/services/my_module.py#MyFactory",
            "method": "non_existent_method",
        }
    },
}

imports = []