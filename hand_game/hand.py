def game_over():
    if computer == user:
       print("\nGame over")
       global exit
       exit = 0
    else:
        exit = 1
    if exit == 1:
        rule()
       
def rule():
    global computer_win
    global user_win
    if user==1 and computer == 2:
        computer_win=computer_win + 1
        print("\nthe win is computer\n")
    elif user== 1 and computer== 3 :
        user_win=user_win+1
        print("\nthe win is user\n")

    elif user == 2 and computer == 1:
        user_win=user_win+1
        print("\nthe win is user\n")

    elif user == 2 and computer == 3:
        computer_win=computer_win + 1
        print("\nthe win is computer\n")

    elif user == 3 and computer == 1:
        computer_win=computer_win + 1
        print("\nthe win is computer\n")

    elif user == 3 and computer == 2:
        user_win=user_win+1
        print("\nthe win is user\n")

    else :
        return
    
    print("\nuser win:",user_win,end="\t")
    print("computer win:",computer_win,end="\n")
        
def display():
    user_thing = thing(user)
    computer_thing=thing(computer)
    print("\nUSER:",user_thing)
    print("COMPUTER:",computer_thing,end="\n") 
    game_over()  

def comp():
    import random
    global computer
    computer = int(random.randint(1,3))
    display()

def thing(x):
    if x == 1:
        x ="rock"
    elif x == 2:
        x="paper"
    elif x == 3:
        x="scissors"
    else:
        pass
    return x

exit = 1
win=0
user_win = 0
computer_win = 0

while exit !=0:
    print("1)rock")
    print("2)paper")
    print("3)scissors")
    global user
    user=int(input("choose your best:"))
    comp()
    
    
     

    
