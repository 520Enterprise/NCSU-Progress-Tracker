flour = input("How much flour do you need?")
sugar = input("How much sugar do you need?")
eggs = input("How many dozen eggs do you need?")
flour = float(flour)
sugar = float(sugar)
eggs = float(eggs)
#@#
pretax = (flour * 3.50) + (sugar * 5.00) + (eggs * 2.10)
tax = (0.07 * ((flour * 3.50) + (sugar * 5.00) + (eggs * 2.10)))
total = (pretax + tax)
print('Total: '+ str(total))
#@#
