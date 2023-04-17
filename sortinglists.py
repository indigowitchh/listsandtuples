import random

num = []

for i in range (0,11):
    num.append(random.randrange(0,100))
    
print(num)

biggest = num[0]
smallest = num[0]

for i in range (0,11):
    if num[i]> biggest:
        biggest = num[i]

for i in range (0,11):
    if num[i]< smallest:
        smallest= num[i]       

num.sort()
mid = num[5]
 
print(num)
print("Biggest number is:", biggest)
print("Smallest number is:", smallest)
print("Mid number is:", mid)
