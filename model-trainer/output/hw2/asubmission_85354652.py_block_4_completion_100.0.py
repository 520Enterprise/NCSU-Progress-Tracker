flour=input("How much flour do you need?")
sugar=input("How much sugar do you need?")
eggs=input("How much eggs do you need?")
flour=float(flour)
sugar=float(sugar)
eggs=float(eggs)
Tflour= flour*3.50
Tsugar= sugar*5.00
Teggs= eggs*2.10
Total=(Tflour+Tsugar+Teggs)
Tax= Total*0.07
print('$'+str(Total+Tax))
