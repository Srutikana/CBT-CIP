import random

print("Welcomw to ROCK PAPER SCISSOR GAME")
user_score=0
comp_score=0
ties=0
name=input("Enter your name here: ")
print("""
Winning Rules:
    1. Paper vs Rock ---> Paper
    2. Rock vs Scissors ---> Rock
    3. Scissors vs Paper ---> Scissor""" )
print(""" Choices are:
        1 = Rock
        2 = Scissor
        3=  Paper""")
while True:
    choice= int(input("Enter your choice between 1-3: "))
    while choice>3 or choice<1:
        choice= int(input("Enter Valid input: "))
    if choice==1:
        user_choice="Rock"
    elif choice==2:
        user_choice="Paper"
    else:
        user_choice="Scissors"
    print(" User's choice is : ",user_choice)
    print("Now it's Computer's turn")
    computer= random.randrange(1,3)
    if computer==1:
        computer_choice="Rock"
    elif computer==2:
        computer_choice="Paper"
    else:
        computer_choice="Scissors"
    print("Computer's Choice is: ",computer_choice)
    if((user_choice =="Paper" and computer_choice == "Rock")or(user_choice=="Rock" and computer_choice=="Paper")):
        print("Paper Wins")
        result = "Paper"
    elif((user_choice =="Scissors" and computer_choice == "Rock")or(user_choice=="Rock" and computer_choice=="Scissors")):
        print("Rock Wins")
        result= "Rock"
    elif(user_choice==computer_choice):
        print("It's a Tie")
        result="Tie"
    else:
        print("Scissors Wins")
        result="Choices"
    if result=="Tie":
        ties+=1
    elif result==user_choice:
        user_score+=1
        print("User Wins")
    else:
        comp_score+=1
        print("Computer Wins")
    print("Scores are")
    print(name,"'s score is: ",user_score)
    print("Compuer's score is: ",comp_score)
    print("Ties are:",ties)
    repeat=input("Do you want to continue??")
    if repeat == "No"or repeat=="no":
        break
print("Game Over")