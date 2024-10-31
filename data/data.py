import random


payload_data = [{
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
        {
        "name": "Apple Ipad",
        "data": {
            "year": 2018,
            "price": 849.99,
        }
    },
        {
        "name": "Apple Iphone XS",
        "data": {
            "year": 2017,
            "price": 700.99,
        }
    }]


payload_data_negative = [{
        "name": "",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "[^!@#$%^&*()_]",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "[^!@#$%^&*()_]",
        "data": {
        }
    }
]

def generate_data():
    return payload_data[random.randint(0,2)]
