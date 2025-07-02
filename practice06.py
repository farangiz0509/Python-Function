

def is_valid_phone_number(phone) :
    if phone == 9 :
        return "true"
    else:
        return "phone number should include 9 numbers"
    

phone = int(input("enter the phone number"))
number = is_valid_phone_number(phone)

print(number)
    