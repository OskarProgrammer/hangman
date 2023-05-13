import os as s
from time import sleep
from random import choice

def check(wyraz,litera,poznane,bledne,copy):
    global proby
    global wartosc
    wyraz=list(wyraz)
    if litera in wyraz:
        s.system("cls")
        print("Correct letter!")
        poznane.append(litera)
        
        while litera in copy:
            if litera in copy:
                copy.remove(litera)
       
        if len(copy)==0:
            s.system("cls")
            print("You won!!!")
            print(f"The chances left --> {proby} !!! ")
            wartosc=1
        wyraz=str(wyraz)

        
        
    
    elif litera not in wyraz:
        
        if proby==0:
            s.system("cls")
            print("Wrong letter!")
            wyraz=list()
            print(f"The word that you had to discover was ")
            for x in range(0,len(wyraz)):
                print(f"{wyraz[x]}",end="")
            print(f"You discovered {len(poznane)} types letters")
            wartosc=1
            print()
            for x in range(0,5):
                print("-",end="")
                if x==4:
                    print("-")
            for x in range(0,4):
                if x==0:
                    print("|    |")
                elif x==1:
                    print("|    O ")
                elif x==2:
                    print("|   / \\")
            for x in range(0,10):
                print("-",end="")
            print()
        
        elif proby!=0:
            
            s.system("cls")
            print("Wrong letter!")
            proby-=1
            bledne.append(litera)
            wyraz=str(wyraz)
    


def output(wyraz,poznane,proby):
    for x in range(0,len(wyraz)):
        if wyraz[x] not in poznane:
            print("_",end=" ")
        elif wyraz[x] in poznane:
            print(f"{wyraz[x]}",end=" ")
        elif wyraz[x] ==" ":
            print(" ",end=" ")
    print("\n")
    print(f"You can mischoose another {proby} times")
    if proby==3:
        for x in range(0,3):
            print("\n")
        print("-----------")
    elif proby==2:
        print("\n")
        for x in range(0,4):
            print("|")
        for x in range(0,10):
            print("-",end="")
        print("\n")
    elif proby==1:
        for x in range(0,5):
            print("-",end="")
            if x==4:
                print("-")
        for x in range(0,4):
            print("|")
        for x in range(0,10):
            print("-",end="")
        print("\n")
    



positive=["yes","YES","Yes","Tak","TAK","tak"]


grupa_losowanie=""
while True:
    grupa_losowanie=""
    poznane=[]
    bledne=[]
    copy=[]
    wartosc=0
    kategoria=""
    s.system("cls")
    print("The game hangman is the type of game in which you have")
    print("to choose the letters from the alfabet to know the random")
    print("word, if you choose correctly the letter the program will place")
    print("this letter on the places where is it in the word")
    print("if you mischoose 3 times in the one session of game you will lose")
    print("Ready?")
    start=input("")
    if start in positive:
        s.system("cls")
        kategoria=input("What will be the category of the word:")
        print(f"The words category--> {kategoria}")
    else:
        continue
    wyraz=input("What is the word that you want to be guessed by others? ")
    print(f"{wyraz}")
    for x in range (0,len(wyraz)):
        if wyraz[x] ==" ":
            continue
        else:
            copy.append(wyraz[x])
    proby=3
    output(wyraz,poznane,proby)
    
    print("\n")
    print(f"You can mischoose another {proby} times")
    litera=""
    while True:
        s.system("cls")
        
        print(f"Category --> {kategoria}")
        output(wyraz,poznane,proby)
        litera=input("Please write a letter ==> ")
        if litera in poznane or litera in bledne:
            print("This letter was already checked")
            sleep(2)
            continue
        
        check(wyraz,litera,poznane,bledne,copy)
        if wartosc==1:
            decyzja=input("Do you still want to play? ")
            if decyzja in positive:
                break
            else:
                s.system("cls")
                print("END GAME")
                exit()
        sleep(2)
        