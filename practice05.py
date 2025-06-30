def check_guess(secret, guess):
    return secret == guess
def print_result(is_correct):
     if is_correct:
         print("togri topdingiz")
     else: 
         print("topolmadingiz")
         
def main():
    secret = 89
    
    guess = int (input("taxmin qililng"))
    
    is_correct = check_guess(secret, guess)
    print_result(is_correct)
    
    main()
        
 
    
 
 