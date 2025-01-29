import random

def generate_password(letters_count, symbols_count, numbers_count, shuffle=True):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    letter_choices = random.choices(letters, k=letters_count)
    symbol_choices = random.choices(symbols, k=symbols_count)
    number_choices = random.choices(numbers, k=numbers_count)
    
    password_list = letter_choices + symbol_choices + number_choices
    
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
