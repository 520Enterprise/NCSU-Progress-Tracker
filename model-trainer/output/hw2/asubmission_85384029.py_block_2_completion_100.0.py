flour1 = input("How much flour do you need? ")
sugar1 = input("How much sugar do you need? ")
eggs1 = input("How many dozen eggs do you need? ")
flour1 = float(flour1)
sugar1 = float(sugar1)
eggs1 = float(eggs1)
priceb4tax = (flour1*3.5) + (sugar1*5.0) + (eggs1*2.1)
total = priceb4tax*1.07
print("The total cost of your cake is " + str(total))
