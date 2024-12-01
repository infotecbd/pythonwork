def validate_name(name):
    if not name.isalpha():
        print("Error: The contact's name must be a string containing only letters.")
        return False
    return True

def validate_phone(phone):
    if not phone.isdigit():
        print("Error: The phone number must be numeric.")
        return False
    return True
