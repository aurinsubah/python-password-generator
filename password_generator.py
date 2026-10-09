import random
import string

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    
    all_chars = letters + digits + symbols
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("=== Simple Password Generator ===")
    try:
        user_length = int(input("Enter desired password length (minimum 8): "))
        if user_length < 8:
            print("Length too short! Setting minimum length to 8.")
            user_length = 8
            
        secure_password = generate_password(user_length)
        print(f"Your secure password is: {secure_password}")
    except ValueError:
        print("Please enter a valid number!")