def is_strong_password(password :str):
    if len(password) >= 8 and password.isalnum() :
        text = "your password is strong"
        return text
    else:
        text = " the password is not strong"
        return text
def main():
    password = input("enter your password: ")
    print(is_strong_password(password))
main()