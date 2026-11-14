import secrets
import string

UC = string.ascii_uppercase
LC = string.ascii_lowercase
DIG = string.digits
SPE = string.punctuation


def generate_password(choice):

    if choice == "1":
        l = 8
        u = UC + LC + DIG
        p = secrets.choice(UC) + secrets.choice(LC) + secrets.choice(DIG)

    elif choice == "2":
        l = 12
        u = UC + LC + DIG + SPE
        p = secrets.choice(UC) + secrets.choice(LC) + secrets.choice(DIG) + secrets.choice(SPE)

    else:
        raise ValueError("Invalid choice")

    for i in range(l - len(p)):
        p += secrets.choice(u)

    password_list = list(p)
    secrets.SystemRandom().shuffle(password_list)
    p = ''.join(password_list)

    return p


def main():

    print("\nChoose Password complexity")
    print("1. Simple")
    print("2. Complex")

    while True:
        choice = input("Enter your choice (1/2): ")

        if choice == "1" or choice == "2":
            break
        else:
            print("Invalid choice!, enter again input")

    p = generate_password(choice)

    print("generated password:", p)


if __name__ == "__main__":
    main()
