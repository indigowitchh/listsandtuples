import random


items = []
def itemDropper():
     num = random.randrange(1, 101)
     if num < 25:
         print("YOu got a potion!")
         items.append("Potion")
     elif num < 50:
         print("You got a sock!")
         items.append("sock")
     elif num < 60:
        print("YOu got el coin!")
        items.append("coin")
     else:
        print("Nothing was received")

while(1 == 1):
    user = input("Press 'c' to continue")
    if user == 'c':
        itemDropper()

