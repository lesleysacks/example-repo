print("Welcome to my gaming quiz!!!\n ")

answer = input("Would you like to play? ").lower()

if answer != "yes":
   print("GOODBYE!")
   quit()
else:
    print("Great :) Let's get ready to play! \nBut firstly.... \n")

name = input("What is your name?:" ).upper()
born = input("Where are you from?:").upper()
print(f"Hi {name} from {born}, I bet you're ready to have some fun? Let's go!!\n ")

answers_correct = 0
#Q1
answer = input("Question 1:What is the smallest country in the world? :")

if answer == "vatican".lower():
    print("Correct! \n")
    answers_correct += 1
else:
    print("Incorrect! \n")

#Q2
answer = input("Question 2:What is the name of the star closest to Earth? :")
if answer == "Sun".lower():
    print("Correct! \n")
    answers_correct += 1
else:
    print("Incorrect! \n")

#Q3
answer = input("Question 3:How many capitals does South Africa have? :")
if answer == "3":
    print("Correct! \n")
    answers_correct += 1
else:
    print("Incorrect! \n")

#Q4
answer = input("Question 4:How many legs does a spider have? :")
if answer == "8" :
    print("Correct! \n")
    answers_correct += 1
else:
    print("Incorrect! \n")

#Q5
answer = input("Question 5:Who painted the Mona Lisa?:")
if answer == "Leonardo da Vinci".lower():
    print("Correct! \n")
    answers_correct += 1
else:
    print("Incorrect!\n")


def show_results(score, total_questions):
    print("\nQuiz complete!")
    print(f"You got {score} out of {total_questions} correct.")
    if answers_correct <= 1:
        print("Your weak!")
    elif answers_correct == 3:
        print("Almost there, hey! Try again!")
    elif answers_correct >= 4:
        print("Top of your class, Great work!")
    

total_questions = 5
show_results(answers_correct, total_questions)
    

    
