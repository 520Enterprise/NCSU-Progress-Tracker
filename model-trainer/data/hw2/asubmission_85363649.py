Flour = 3.50
Sugar = 5.00
Eggs = 2.10
Flour2 = input("How much flour do you need?: ")
Sugar2 = input("How much sugar do you need?: ")
Eggs2 = input("How many dozen eggs do you need?: ")
#@#
Flour2 = float(Flour2)
Sugar2 = float(Sugar2)
Eggs2 = float(Eggs2)
#@#
flour_total = (Flour * Flour2)
sugar_total = (Sugar * Sugar2)
eggs_total = (Eggs * Eggs2)
#@#
pretax_total = (flour_total + sugar_total + eggs_total)
tax_amt = (pretax_total * .07)
subtotal = (pretax_total + tax_amt)
print("Total: $" + str(subtotal))
#@#