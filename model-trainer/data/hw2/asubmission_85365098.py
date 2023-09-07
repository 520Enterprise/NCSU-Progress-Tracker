flour = 3.50
sugar = 5.00
eggs = 2.10
flour2 = input("How much flour do you need?")
sugar2 = input ("How much sugar do you need?")
eggs2 = input ("How many eggs do you need by the dozen?")
#@#
flour2 = float(flour2)
sugar2 = float(sugar2)
eggs2 = float(eggs2)
#@#
subtotal = (flour*flour2)+(eggs*eggs2)+(sugar*sugar2)
#@#
subtotal2 = (subtotal*.07)+subtotal
print ('Total: $'+str(subtotal2))
#@#
