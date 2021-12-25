import random 
from time import sleep
count  = 1 
while True:
    my_num = input("Number 1 to 10 : ")
    g_num = random.randint(1,10)
    if g_num == int(my_num):
        print(f" After {count} times lost")
        sleep(1)
        print("Congratulation , finally You Win !!")
        break
    else:
        print(f"{my_num} that a Wrong Number")
        
        sleep(1)
        print(".")
        sleep(1)
        print("...")
        sleep(1)
        print()
        print("Try Again , May Be You Win Next Try")
        count += 1
        continue
