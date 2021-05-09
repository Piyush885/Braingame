import random
import pyautogui
import playsound
import time
import os
x="Piysuh Rai welcome you to this brain game\nThanks to give your time\n"
time.sleep(0.3)
name=str(input("Enter Your Name-----"))
print("\n")
for i in x:
    print(i,end="")
    time.sleep(0.008)
print("-------------------------Rule----------------------------------------")
print("\n")
time.sleep(0.3)
z="Given a number 15. You and Computer which is your opponent have to make this number zero\nyou and computer both will get chance one after the other.Both have to select 1 or 2\nIf you select 1 then 1 is minus from original number and same for 2.Then computer will select\nThe last candidate who makes the number zero wins the game\n"
for i in z:
    print(i,end="")
    time.sleep(0.008)
print("Warning---If you will select an invalid choice then game will end automatically.So donot try this for fun\n")
print("Your task is to find best strategy of the game so that you beat the computer every time.\n")
print("\n")
s="y"
while(s=="y" or s=="Y"):
    n=15
    win=0
    a=int(input("*******  If you want to take first chance press  1 otherwise press 2  ***********\n"))
    os.system('cls')
    playsound.playsound("Whistle Kbc 4.mp3")
    time.sleep(0.3)
    print("Lets begin.Good Luck ",name)
    if a == 1:
        while(n>0):
            op=int(input(" your turn:- "))
            n=n-op
            if (op !=1 and op !=2):
               print("Wrong Choice.Please restart game and select only 1 or 2--")
               exit()
            #else:
            if(n%3==2):
                print("computer selected 2")
                win=1
                n=n-2
                print("New number is--\n",n)
                continue
            elif(n%3==1):
                print("computer selected 1")
                win=1
                n=n-1
                print("New number is--\n",n)
                continue
            
            else:
                break
    elif (a==2):
        while(n>0):
            if(n%3 == 2):
                print("computer selected 2")
                n=n-2
                print("New number is ",n)
                win=1
            elif(n%3==1):
                print("computer selected 1")
                n=n-1
                print("New number is ",n)
                win=1
            elif(n%3 == 0 and n>0):
                r=random.randint(1,2)
                print("computer selected",r)
                n=n-r
                print("New number is ",n)
                win=1
            if n>0:
            
                op=int(input("Your Turn:- "))
                if(op != 1 and op !=2):
                    print("wrong choice!!Restart game and select only 1 or 2--")
                    exit()
                else:    
                    n=n-op
                    if  n==0:
                        win=0
                        break

    else:
        print("Please select only 1 or 2!!")
        print("Restart game and try again")
        exit()
    if win == 0:
        w="---------------------Congratulates !!!!!!!  You beat the computer-----------------------------------\n"
        for i in w:
            print(i,end="")
            time.sleep(0.008)
        playsound.playsound("KBC Background Sounds ! KBC Sound Effects ! Kaun Banega Crorepati Sound Effects.mp3")    
    else:
        playsound.playsound("Kbc 2010.mp3")
        l="----------------------You Lose.Better Luck Next Time------------------------------------------------\n"
        for i in l:
            print(i,end="")
            time.sleep(0.008)
            
    print(name,end=" ")                      
    s=str(input(" do you want to play again press y else press n\n"))
    os.system('cls')
    
    
