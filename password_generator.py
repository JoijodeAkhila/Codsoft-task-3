import random
import string
def generate_password(length):
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers="0123456789"
    symbols="{}!@$#%^&*()_-+?|"
    all=lower+upper+numbers+symbols
    password=[
        random.choice(lower),
        random.choice(upper),
        random.choice(numbers),
        random.choice(symbols)
        ]
    password += random.choices(all, k=length-4)
    random.shuffle(password)
    return ''.join(password)
def main():
    while True:
        try:
            length=int(input("Enter password length(minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Please enter valid number.")
    num_passwords = int(input("How many passwords do you want to generate? "))
    for i in range(num_passwords):
        password = generate_password(length)
        print(f"Password {i+1}: {password}")
    print("\nPassword generator complete.")
if __name__ =="__main__":
    main()
