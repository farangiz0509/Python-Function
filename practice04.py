

def get_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 50 <= score <= 59:
        return "E"
    else:
        return "error"
    
    
        
score = int(input("enter your score : "))
grade = get_grade(score)
        
print(grade)
    
    
