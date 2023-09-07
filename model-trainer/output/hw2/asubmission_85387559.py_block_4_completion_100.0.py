flour=input("How much flour do you need?")
sugar=input("How much sugar do you need?")
eggs=input("How many dozen eggs do you need?")
flour=float(flour)
sugar=float(sugar)
eggs=float(eggs)
flourcost=flour*3.50
sugarcost=sugar*5.00
eggcost=eggs*2.10
subtotal=flourcost+sugarcost+eggcost
print(subtotal)
tax=subtotal*.07
total=subtotal+tax
print(total)
