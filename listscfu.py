pets = []
favfood = ['sushi', 'ramen', 'poke', 'enchiladas', 'sttacos', 'pandulce','pineapple','mango']
print(favfood[2])
favfood.append('strawberry')
print(len(favfood))
print(favfood)


choice = input("Enter your pets name:")
while choice != 'quit':
    pets.append(choice)
    choice = input("Continue the list or type quit:")
    pets.sort()
else:
    print("Thank you goodbye!")
print(pets)
