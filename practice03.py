

def is_even(number):
    return number % 2 == 0
    
    
def print_even_message(number):

    print (f" {number} is even num")
    
def print_odd_message(number):
    
    print(f"{number} is odd num ")
    
def main():
    number = int(input ("enter the number"))
    if is_even(number):
     print_even_message(number)
         
          
    else :
      print_odd_message(number)
          
main()    

    

     