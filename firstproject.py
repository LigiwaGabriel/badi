# GUESSING GAME 
print("Hello there, What is your name?")
name=input("Enter your name")
print("Welcome back!",name)
print("I am going to describe for you one of your friends from class and you should guess them")
print("The pserson is tall, brown, and funny")
print("Who is that person")

Person="Moses"
guess=input("Guess the person")
while guess!=Person:
    print("Thats incorrect, Try again")
    guess=input("Guess the person")

if (guess=="Moses"):
    print("Thats correct! Wanna Play again?")





