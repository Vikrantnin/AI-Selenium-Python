def generate_login_data():

    test_cases = [
        ("valid_user@gmail.com", "valid@123"),   # Positive
        ("invalid_user@gmail.com", "wrongpassword"), # Invalid credentials
        ("", "password123"),                         # Blank username
        ("user@gmail.com", "")                       # Blank password
    ]

    return test_cases