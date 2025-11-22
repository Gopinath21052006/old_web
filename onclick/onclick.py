import random
def display(total):
    print("\t\t\t\t\t",total)
print("1)increase")
print("2)decrease")
print("3)reset")
print("4)random")
print("5)exit")
total =0
choose =0
while choose!=5 :
    choose=int(input("Enter you choose:"))
    if choose == 1:
        total+=1
        display(total)
    elif choose == 2:
        total-=1
        display(total)
    elif choose == 3:
        total =0
        display(total)
    elif choose ==4:
        total= random.randrange(0,100)
        display(total)
    else:
        print("please enter the correct choose")
        choose=int(input("Enter you choose:"))
    print("1)increase \t 2)decrease \t 3)reset \t 4)random \t 5)exit")

        