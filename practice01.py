

def add(a, b):
    z = a + b
    return z
    
def subtract(a, b):
    z = a - b
    return z
    
def multiply(a, b):
    z = a * b
    return z
    
def divide(a, b):
    z = a / b
    return z

def main():
    a = int(input("enter the number : "))
    b = int (input("enter the number_2 :"))
    operators = input("operators (+ , - , *, /, )")
    
    if operators == "+":
        print(add(a ,b))
    elif operators == "-":
        print(subtract(a ,b))
    elif operators == "*":
        print(multiply(a, b))
    elif operators == "/":
        print(divide(a ,b))
    else:
        print("wrong operator")
        
main()
        
    
     