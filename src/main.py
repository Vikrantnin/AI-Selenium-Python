def generate_login_data():

    test_cases = [
        ("valid_user@gmail.com", "validpass@321"),   # Positive
        ("invalid_user@gmail.com", "wrongpass123"), # Invalid credentials
        ("", "password123"),                         # Blank username
        ("username@gmail.com", "")                       # Blank password
    ]

    return test_cases