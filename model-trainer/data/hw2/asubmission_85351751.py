flour = 3.50
sugar = 5.00
eggs = 2.10
flourQuant = input('How much flour do you need? ')
sugarQuant = input('How much sugar do you need? ')
eggQuant = input('How many dozen eggs do you need? ')
#@#
subTotal = flour * int(flourQuant) + sugar * int(sugarQuant) + eggs * int(eggQuant)
#@#
totalCost = (subTotal * 0.07) + subTotal
print("Total: $" + str(totalCost))
#@#
