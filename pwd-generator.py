import random
import string

def generate_password(length=12):
    """Generate a random password with a mix of characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate and print a 12-character password
new_password = generate_password()
print(f"Your new password is: {new_password}")
