import unittest
import sys

sys.path.append("C:\\bin\\rack_code_challenge\\lib")
from store import *

class test_customers(unittest.TestCase):

    def setUp(self):

        lst1 = Helper.getFileContents("inputFiles/ex2.txt")

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

        for i, each in enumerate(self.custs):

            if i % 2 == 0:
                self.assertTrue( isinstance(each, TypeACustomer) )
            else:
                self.assertTrue( isinstance(each, TypeBCustomer) )
    #end method

    def test_integration(self):
        
        while not self.store.isEmpty():
            
            ct = self.store.incrementTime()

            for each in self.store.registers:
                each.checkout()

            currentArrivals = self.store.checkArrivals(ct, self.store.customers)
            whoPicks = self.store.whoPicks(currentArrivals)

            if whoPicks:
                register = whoPicks.pickLine(self.store.registers)
                register.addCustomer(whoPicks)
            else:
                register = self.store._registers[0]

        #end loop

        print("Finished at: t={0} minutes".format(self.store._elapsed_time))

    #end method

#end class

if __name__ == '__main__':
    unittest.main()