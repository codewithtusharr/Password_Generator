import random
import string

def generate_password(length=25):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example: Generate a password with default length (12 characters)
password = generate_password()
print("Generated Password:", password)