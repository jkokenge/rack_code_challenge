import unittest
import sys

sys.path.append("C:\\bin\\rack_code_challenge\\lib")
from store import *


class test_customers(unittest.TestCase):

    def setUp(self):

        lst1 = Helper.getFileContents("inputFiles/ex1.txt")

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

        self.assertTrue( isinstance(self.registers[0], TrainingCashier) )
        self.assertTrue( self.registers[0]._time_per_item == 2 )

    #end method

    def test_customers(self):
        for each in self.custs:
            self.assertTrue( isinstance(each, TypeACustomer) )
    #end method

    def test_customer_behavior(self):
        
        currentTime = self.store._elapsed_time
        self.assertTrue( currentTime == 0 )

        currentTime = self.store.incrementTime()
        self.assertTrue( currentTime == 1 )

        currentArrivals = self.store.checkArrivals(currentTime, self.store.customers)
        self.assertTrue( len(currentArrivals) == 1 )
        self.assertTrue( currentArrivals[0] == self.store.customers[0] )
        
        whoPicks = self.store.whoPicks(currentArrivals)
        self.assertTrue( whoPicks == self.store.customers[0] )

        register = whoPicks.pickLine(self.store.registers)
        self.assertTrue( register == self.store.registers[0] )
        register.addCustomer(whoPicks)
        self.assertTrue( register._customers[0] == whoPicks )
        self.assertTrue( whoPicks in register )
        self.assertTrue( len(register._customers) == 1 )

        #TO DO implement the correct checkout process
        register.checkout()
        print("currentTime {}".format(currentTime))
        self.assertTrue( whoPicks._items == 2)

        currentTime = self.store.incrementTime()
        currentArrivals = self.store.checkArrivals(currentTime, self.store.customers)
        self.assertTrue( len(currentArrivals) == 1 )
        self.assertTrue( currentArrivals[0] == self.store.customers[1] )

        whoPicks = self.store.whoPicks(currentArrivals)
        self.assertTrue( whoPicks == self.store.customers[1] )

        register = whoPicks.pickLine(self.store.registers)
        self.assertTrue( register == self.store.registers[0] )

        register.addCustomer(whoPicks)
        print(register._customers)
        self.assertTrue( register._customers[1] == whoPicks )
        self.assertTrue( whoPicks in register )

        register.checkout()
        print("currentTime {}".format(currentTime))
        self.assertTrue( register._customers[0]._items == 2)

        currentTime = self.store.incrementTime()
        self.assertTrue( currentTime == 3 )

        register.checkout()
        print("currentTime {}".format(currentTime))
        self.assertTrue( register._customers[0]._items == 1)

        currentTime = self.store.incrementTime()
        self.assertTrue( currentTime == 4 )
        register.checkout()
        print("currentTime {}".format(currentTime))
        self.assertTrue( register._customers[0]._items == 1)

        currentTime = self.store.incrementTime()
        self.assertTrue( currentTime == 5 )
        register.checkout()
        print("currentTime {}".format(currentTime))
        print( register._customers )
        self.assertTrue( register._customers[0] == self.store.customers[0])
        print(self.store.customers[0])
        
        currentTime = self.store.incrementTime()
        self.assertTrue( currentTime == 6 )
        register.checkout()
        print("currentTime {}".format(currentTime))
        print( register._customers )
        #self.assertTrue( register._customers[0]._items == 1)

    #end method

#end class

if __name__ == '__main__':
    unittest.main()