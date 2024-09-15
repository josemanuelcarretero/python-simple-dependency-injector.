services = {
    "another_service": {
        "class": "tests/services/my_module.py#AnotherService",
        "arguments": [
            "@core_service",
            "!tagged service",
            "!context",
        ],
    },
    "core_service": {"class": "tests/services/my_module.py#CoreService", "tags": ["service"]},
    "base_service": {"class": "tests/services/my_module.py#BaseService", "tags": ["service"]},
}

imports = []
