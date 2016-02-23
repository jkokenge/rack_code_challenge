import sys
from lib.store import *

path = sys.argv[1]

lst1 = Helper.getFileContents(path)

store1 = GroceryStore()

registers = Helper.getRegisters(int(lst1[0]), store1)
del lst1[0]

custs = []

for each in lst1:
    type, arrived, items = tuple(each.split())
    custs.append(Helper.customerType(type, arrived, items))
#end loop

store1.registers = registers
store1.customers = custs

while not store1.isEmpty():
            
    ct = store1.incrementTime()

    currentArrivals = store1.checkArrivals(ct, store1.customers)

    for each in store1.registers:
        each.checkout()
    #end loop

    whoPicks = store1.whoPicks(currentArrivals)

    if len(currentArrivals) > 1:

        for each in whoPicks:
                    
            register = each.pickLine(store1.registers)
            register.addCustomer(each)
        #end loop
    else:
            
        if whoPicks != False:
                
            register = whoPicks.pickLine(store1.registers)
            register.addCustomer(whoPicks)
        #end if
    #end if/else            

#end loop

print("Finished at: t={0} minutes".format(store1._elapsed_time))