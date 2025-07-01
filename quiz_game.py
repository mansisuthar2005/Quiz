from colorama import init, Fore
init(autoreset=True)
print("Welcome to my computer quiz!💻")
total1=0
while True:
    print(Fore.LIGHTBLUE_EX+'1.Want to play.')
    print(Fore.LIGHTBLUE_EX+'2.Not interested.')
    playing=int(input(Fore.BLUE+'ENTER YOUR CHOICE:'))     
    if playing==1:
        print(Fore.CYAN+"Okay! Let's play :)🚀")
        score=0
        answer = input("What is the full form of CPU? ")
        if answer.lower() == "central processing unit":
            print(Fore.GREEN+"correct✔")
            score+=1
        else:
            print(Fore.RED+'Incorrect❌')
        answer = input("What does GPU stand for? ")
        if answer.lower() == "graphics processing unit":
            print(Fore.GREEN+"correct✔")
            score+=1
        else:
            print(Fore.RED+'Incorrect❌')
        answer = input("What is the full form of RAM? ")
        if answer.lower() == "random access memory":
            print(Fore.GREEN+"correct✔")
            score+=1
        else:
            print(Fore.RED+'Incorrect❌')  
        answer = input("What is the full form of PSU? ")
        if answer.lower() == "power supply":
            print(Fore.GREEN+"correct✔")
            score+=1
        else:
            print(Fore.RED+'Incorrect❌')

        answer = input("What is the full form of ROM? ")
        if answer.lower() == "read only memory":
            print(Fore.GREEN+"correct✔")
            score+=1
        
        else:
            print(Fore.RED+'Incorrect❌')
        print(Fore.YELLOW+'You score is:',score,end=" ")
        print(Fore.YELLOW+'out of 5📄.')
        total1+=1
        

    elif playing==2:
        print(Fore.GREEN+'No Worries.😊')
        if total1>0:
            print(Fore.GREEN+'THANK YOU FOR PLAYING THIS GAME🤗.\n')
        break
    else:
        print(Fore.RED+'Invalid choice')
    score+=1;

