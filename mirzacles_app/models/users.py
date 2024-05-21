users_db = {
    "johndoe": {
        "id": 1,
        "username": "johndoe",
        "firstname": "john",
        "lastname": "doe",
        "hashed_password": "cb6ef2e790c2f65247065045e16070f27d9097a417cc4ef65ff9e6494a4f9ca9",
        "email": "johndoe@mailinator.com",
        "active": True,
        "created_at": "2022-11-25"
    },
    "aliceblue": {
        "id": 2,
        "username": "aliceblue",
        "firstname": "Alice",
        "lastname": "Blue",
        "hashed_password": "dead7c650746837306284dd73015e2d1c88e2d5d8b48cd732b4e52d0f7c238a4",
        "email": "alice@mailinator.com",
        "active": True,
        "created_at": "2022-11-25"
    },
}


permissions_db = {
    1 : {
        "user_id": 1,
        "permissions": ["users"]
    },
    2 : {
        "user_id": 2,
        "permissions": ["items"]
    },
}
