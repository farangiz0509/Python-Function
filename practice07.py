


def ask_question(question):
    user_answer = input(f"{question} ").strip()
    return user_answer

def check_answer(user_answer, correct_answer):
    result = user_answer.lower() == correct_answer.lower()
    return result

def main():
    question = "what has a neck but not head?"
    correct_answer = "bottle"

    user_answer = ask_question(question)
    is_correct = check_answer(user_answer, correct_answer)

    if is_correct:
        print("correct")
    else:
        print(f"wrong , correct answer is \"{correct_answer}\"")

main()