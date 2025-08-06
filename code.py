total_qns=5
questions_and_ans = {
    "What is the capital of France?": {"answer": "Paris"},
    "Which language is primarily used for Android app development?": {"answer": "Java"},
    "What does CPU stand for?": {"answer": "Central Processing Unit"},
    "Who wrote the play 'Romeo and Juliet'?": {"answer": "William Shakespeare"},
    "The boiling point of water at sea level is ______°C?": {"answer": "100"}
}




name=input("What's your name : ").capitalize()
print(f"Hey there {name}!, Welcome to the quiz")
ready = input("Are you ready to begin the quizz? (y/n): ").lower()



if ready == "y":
    print("Alright lets begin")

    score = 0

    for question, answer in questions_and_ans.items():
        user_answer = input(question + " ")
        correct_ans= answer["answer"]
        if user_answer.strip().lower() == correct_ans.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_ans}.\n")

    print(f"\nYour final score is {score}/{total_qns}.")

    if score >= 4:
        print(f"You did Good! Congrats {name}\n")


else:
    print("Come back when you are ready!! Bye for now")