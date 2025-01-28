def convert(input_str):
    """
    Converts :) to 🙂 and :( to 🙁 in the input string.
    """
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    """
    Prompts the user for input, converts the text, and prints the result.
    """
    user_input = input("Enter your text: ")
    result = convert(user_input)
    print(result)

# Change _name_ to __name__
if __name__ == "__main__":  # Corrected the variable name
    main()
