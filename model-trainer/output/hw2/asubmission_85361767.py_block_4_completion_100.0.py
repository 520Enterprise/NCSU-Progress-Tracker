flour=input("How much flour do you need?")
sugar=input("How much sugar do you need?")
eggs=input("How many dozen of eggs do you need?")
flour=float(flour)
sugar=float(sugar)
eggs=float(eggs)
flour_c=flour*3.50
sugar_c=sugar*5
eggs_c=eggs*2.10
subtotal=flour_c+sugar_c+eggs_c
sales_tax=subtotal*.07
total=subtotal+sales_tax
print(total)
