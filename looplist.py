colors = ["pink", "purple", "black", "indigo", "turqoise"]
paychecks = [296.80, 280.60, 263.30, 300.61]
foods = []

print(colors[0], colors[2], colors[4])
colors.append("white")
print(colors)


sum = 0
for i in range (len(paychecks)):
    sum+= paychecks[i]
print(sum)


yum = int(input("How many types of foods do you want to take to Mars:"))
for i in range (yum):
    type=input("Type the food you want:")
    foods.append(type)
print(foods)
