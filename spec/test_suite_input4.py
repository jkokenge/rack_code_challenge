import unittest
import sys

sys.path.append("C:\\bin\\rack_code_challenge\\lib")
from store import *

class test_customers(unittest.TestCase):

    def setUp(self):

        lst1 = Helper.getFileContents("inputFiles/ex4.txt")

        self.store = GroceryStore()

        self.registers = Helper.getRegisters(int(lst1[0]), self.store)
        del lst1[0]

        self.custs = []

        for each in lst1:
            type, arrived, items = tuple(each.split())
            self.custs.append(Helper.customerType(type, arrived, items))
        #end loop

        self.store.registers = self.registers
        self.store.customers = self.custs

    #end set up method

    def test_registers(self):

        self.assertTrue( isinstance(self.registers[0], Cashier) )
        self.assertTrue( isinstance(self.registers[1], TrainingCashier) )
        self.assertTrue( self.registers[1]._time_per_item == 2 )

    #end method

    def test_customers(self):

        for each in self.custs:
            self.assertTrue( isinstance(each, TypeACustomer) )
        #end loop
            
    #end method

    def test_integration(self):
        
        while not self.store.isEmpty():
            
            ct = self.store.incrementTime()

            currentArrivals = self.store.checkArrivals(ct, self.store.customers)

            for each in self.store.registers:
                each.checkout()
            #end loop

            if len(currentArrivals) > 1:
                
                for each in currentArrivals:
                    register = each.pickLine(self.store.registers)
                    register.addCustomer(each)
                #end loop
            else:

                whoPicks = self.store.whoPicks(currentArrivals)
            
                if whoPicks != False:
                
                    register = whoPicks.pickLine(self.store.registers)
                    register.addCustomer(whoPicks)
                #end if
            #end if/else            

            #print("elapsed time is {0} \n{1}".format(ct, self.store))

            #if ct < 16:
            #    x = raw_input("")

        #end loop

        print("Finished at: t={0} minutes".format(self.store._elapsed_time))

    #end method

#end class

if __name__ == '__main__':
    unittest.main()