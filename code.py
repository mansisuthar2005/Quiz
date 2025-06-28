print("Welcome to my computer quiz!");
playing=input("Do you want to play? ");
if playing.lower == "no":
    quit();
print("Okay! Let's play :) ");
print("Make sure you write the full answers in small letters only");

answer = input("What is the full form of CPU? ");
if answer == "central processing unit":
    print("correct!");
else:
    print('Incorrect');
answer = input("What does GPU stand for? ");
if answer == "graphics processing unit":
    print("correct!");
else:
    print('Incorrect');
answer = input("What is the full form of RAM? ");
if answer == "random access memory":
    print("correct!");
else:
    print('Incorrect');    
answer = input("What is the full form of PSU? ");
if answer == "power supply":
    print("correct!");
else:
    print('Incorrect');

answer = input("What is the full form of ROM? ");
if answer == "read only memory":
    print("correct!");
else:
    print('Incorrect');
