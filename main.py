def main():
    encoded_password = ""
    password = ""

    while True:
        print("\nMenu")
        print("-------------")
        print("1. Encode password")
        print("2. Decode password")
        print("3. Quit\n")
        choice = input("Please enter an option:")  # Users can enter their choice after the menu is displayed.

        if choice == "1":
            password = input("Enter password to encode: ")
            encoded_password = encode(password) # Stores the password and user is made aware
            print("Your password has been encoded and stored!")

        elif choice == "2":
            if encoded_password:
                decoded_password = decode(encoded_password)
                print("The encoded password is {}, and the original password is {}.".format(encoded_password,
                                                                                           decoded_password))

            else:
                print("Please encode a password first.")  # I added an option in case the user picked 2 before 1


        elif choice == "3":
            break  # program stops if option 3 is chosen

        else:
            print("Invalid choice. Please try again.")


def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit
    return encoded_password


if __name__ == "__main__":
    main()
