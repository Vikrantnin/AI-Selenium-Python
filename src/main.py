def generate_login_data():

    test_cases = [
        ("valid_user@gmail.com", "validpassword"),
        ("invalid_user@gmail.com", "wrongpassword"),
        ("", "password123"),
        ("user@gmail.com", "")
    ]

    return test_cases