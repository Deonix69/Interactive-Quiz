score = 0
correct = 0

def main(score, correct):
    print("Hello welcome to (Basic Name) Quiz!")
    start_quiz = input("Type start to start the quiz: ")
    if start_quiz == "start":
        print("You have selected to start the quiz")

    else:
        print("Have a good day!")

    print("Question One: What 1+1?")
    answer1 = input("")
    if answer1 == "2":
        score += 20
        correct += 1
        print("Correct!")
    else:
        score += 0
        correct += 0
        print("Incorrect!")

    print("Question Two: What color is the sun?")
    answer2 = input("")
    if answer2 == "Yellow":
        score += 20
        correct += 1
        print("Correct!")
    else:
        score += 0
        correct += 0
        print("Incorrect!")

    print("Question Three: What is the capital of the USA?")
    answer3 = input("")
    if answer3 == "Washington D.C.":
        score += 20
        correct += 1
        print("Correct!")
    else:
        score += 0
        correct += 0
        print("Incorrect!")

    print("Question Four: What is the name of someone who teaches?")
    answer4 = input("")
    if answer4 == "Teacher":
        score += 20
        correct += 1
        print("Correct!")
    else:
        score += 0
        correct += 0
        print("Incorrect!")

    print("Question Five: Who is a man's best friend?")
    answer5 = input("")
    if answer5 == "Dog":
        score += 20
        correct += 1
        print("Correct!")
    else:
        score += 0
        correct += 0
        print("Incorrect!")

    print("You finished the quiz!")
    print(f"You scored a {score} and got {correct} correct!")



main(score, correct)
