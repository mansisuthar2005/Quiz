from colorama import init, Fore
init(autoreset=True)
print("Welcome to my computer quiz!");
playing=input("Do you want to play? ");
if playing.lower == "no":
    quit();
print(Fore.CYAN+"Okay! Let's play :)\nMake sure you write the full answers in small letters only");
score=0;
answer = input("What is the full form of CPU? ");
if answer == "central processing unit":
    print(Fore.GREEN+"correct!");
    score+=1;
else:
    print(Fore.RED+'Incorrect');
answer = input("What does GPU stand for? ");
if answer == "graphics processing unit":
    print(Fore.GREEN+"correct!");
    score+=1;
else:
    print(Fore.RED+'Incorrect');
answer = input("What is the full form of RAM? ");
if answer == "random access memory":
    print(Fore.GREEN+"correct!");
    score+=1;
else:
    print(Fore.RED+'Incorrect');    
answer = input("What is the full form of PSU? ");
if answer == "power supply":
    print(Fore.GREEN+"correct!");
    score+=1;
else:
    print(Fore.RED+'Incorrect');

answer = input("What is the full form of ROM? ");
if answer == "read only memory":
    print(Fore.GREEN+"correct!");
    score+=1;
else:
    print(Fore.RED+'Incorrect');
print(Fore.YELLOW+'You score is:',score,end=" ");
print(Fore.YELLOW+'out of 5.');
print(Fore.GREEN+'THANK YOU FOR PLAYING THIS GAME');
