Flour = 3.50
Sugar = 5.00
Eggs = 2.10
Flour2 = input("How much flour do you need? ")
Sugar2 = input("How much sugar do you need? ")
Eggs2 = input("How many dozen eggs do you need? ")
#@#
Flour2 = float(Flour2)
Sugar2 = float(Sugar2)
Eggs2 = float(Eggs2)
#@#
Total1 = (((Flour*Flour2) + (Sugar*Sugar2) + (Eggs*Eggs2))*.07)
Total2 = ((Flour*Flour2) + (Sugar*Sugar2) + (Eggs*Eggs2))
#@#
Total1 = float(Total1)
Total2 = float(Total2)
print("Total: $" + str(Total1 + Total2))
#@#
