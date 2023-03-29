def main():
    encoded_password = ""  # Define variable outside of if blocks
    password = ""  # Define variable outside of if blocks

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode password")
        print("2. Decode password")
        print("3. Quit\n")
        choice = input("Please enter an option:")

        if choice == "1":
            password = input("Enter password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")

        elif choice == "2":
            if encoded_password:
                decoded_password = decode(encoded_password)
                print("The encoded password is {}, and the original password is {}.".format(encoded_password,
                                                                                           decoded_password))

            else:
                print("Please encode a password first.")


        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")


def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        decoded_password += decoded_digit
    return decoded_password

if __name__ == "__main__":
    main()

