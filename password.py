import random
import string

def generate_password(letters_count, symbols_count, numbers_count, shuffle=True):
    letters = random.choices(string.ascii_letters, k=letters_count)
    symbols = random.choices("!@#$%^&*()-_=+[]{};:,.<>?/", k=symbols_count)
    numbers = random.choices(string.digits, k=numbers_count)

    password_list = letters + symbols + numbers

    if shuffle:
        random.shuffle(password_list)

    return "".join(password_list)

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")

def main():
    letters_count = get_positive_integer("How many letters would you like in your password? ")
    symbols_count = get_positive_integer("How many symbols would you like? ")
    numbers_count = get_positive_integer("How many numbers would you like? ")

    ordered_password = generate_password(letters_count, symbols_count, numbers_count, shuffle=False)
    shuffled_password = generate_password(letters_count, symbols_count, numbers_count, shuffle=True)

    print(f"Ordered password: {ordered_password}")
    print(f"Shuffled password: {shuffled_password}")

if __name__ == "__main__":
    main()
