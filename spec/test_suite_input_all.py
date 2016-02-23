import unittest
import sys

sys.path.append("C:\\bin\\rack_code_challenge\\lib")
from store import *

class test_customers(unittest.TestCase):

    def setUp(self):

        lst1 = Helper.getFileContents("inputFiles/ex1.txt")

        self.store1 = GroceryStore()

        registers = Helper.getRegisters(int(lst1[0]), self.store1)
        del lst1[0]

        custs = []

        for each in lst1:
            type, arrived, items = tuple(each.split())
            custs.append(Helper.customerType(type, arrived, items))
        #end loop

        self.store1.registers = registers
        self.store1.customers = custs

        ###################################################

        lst1 = Helper.getFileContents("inputFiles/ex2.txt")

        self.store2 = GroceryStore()

        registers = Helper.getRegisters(int(lst1[0]), self.store2)
        del lst1[0]

        custs = []

        for each in lst1:
            type, arrived, items = tuple(each.split())
            custs.append(Helper.customerType(type, arrived, items))
        #end loop

        self.store2.registers = registers
        self.store2.customers = custs

        ###################################################

        lst1 = Helper.getFileContents("inputFiles/ex3.txt")

        self.store3 = GroceryStore()

        registers = Helper.getRegisters(int(lst1[0]), self.store3)
        del lst1[0]

        custs = []

        for each in lst1:
            type, arrived, items = tuple(each.split())
            custs.append(Helper.customerType(type, arrived, items))
        #end loop

        self.store3.registers = registers
        self.store3.customers = custs

        ###################################################

        lst1 = Helper.getFileContents("inputFiles/ex4.txt")

        self.store4 = GroceryStore()

        registers = Helper.getRegisters(int(lst1[0]), self.store4)
        del lst1[0]

        custs = []

        for each in lst1:
            type, arrived, items = tuple(each.split())
            custs.append(Helper.customerType(type, arrived, items))
        #end loop

        self.store4.registers = registers
        self.store4.customers = custs

        ###################################################

        lst1 = Helper.getFileContents("inputFiles/ex5.txt")

        self.store5 = GroceryStore()

        registers = Helper.getRegisters(int(lst1[0]), self.store5)
        del lst1[0]

        custs = []

        for each in lst1:
            type, arrived, items = tuple(each.split())
            custs.append(Helper.customerType(type, arrived, items))
        #end loop

        self.store5.registers = registers
        self.store5.customers = custs

    #end set up method

    def test_integration_1(self):
        
        while not self.store1.isEmpty():
            
            ct = self.store1.incrementTime()

            currentArrivals = self.store1.checkArrivals(ct, self.store1.customers)

            for each in self.store1.registers:
                each.checkout()
            #end loop

            whoPicks = self.store1.whoPicks(currentArrivals)

            if len(currentArrivals) > 1:

                for each in whoPicks:
                    
                    register = each.pickLine(self.store1.registers)
                    register.addCustomer(each)
                #end loop
            else:
            
                if whoPicks != False:
                
                    register = whoPicks.pickLine(self.store1.registers)
                    register.addCustomer(whoPicks)
                #end if
            #end if/else            

        #end loop

        print("Finished at: t={0} minutes".format(self.store1._elapsed_time))
        self.assertTrue( self.store1._elapsed_time == 7 )

    #end method

    def test_integration_2(self):
        
        while not self.store2.isEmpty():
            
            ct = self.store2.incrementTime()

            currentArrivals = self.store2.checkArrivals(ct, self.store2.customers)

            for each in self.store2.registers:
                each.checkout()
            #end loop

            whoPicks = self.store2.whoPicks(currentArrivals)

            if len(currentArrivals) > 1:

                for each in whoPicks:
                    
                    register = each.pickLine(self.store2.registers)
                    register.addCustomer(each)
                #end loop
            else:
            
                if whoPicks != False:
                
                    register = whoPicks.pickLine(self.store2.registers)
                    register.addCustomer(whoPicks)
                #end if
            #end if/else            

        #end loop

        print("Finished at: t={0} minutes".format(self.store2._elapsed_time))
        self.assertTrue( self.store2._elapsed_time == 13 )

    #end method

    def test_integration_3(self):
        
        while not self.store3.isEmpty():
            
            ct = self.store3.incrementTime()

            currentArrivals = self.store3.checkArrivals(ct, self.store3.customers)

            for each in self.store3.registers:
                each.checkout()
            #end loop

            whoPicks = self.store3.whoPicks(currentArrivals)

            if len(currentArrivals) > 1:

                for each in whoPicks:
                    
                    register = each.pickLine(self.store3.registers)
                    register.addCustomer(each)
                #end loop
            else:
            
                if whoPicks != False:
                
                    register = whoPicks.pickLine(self.store3.registers)
                    register.addCustomer(whoPicks)
                #end if
            #end if/else            

        #end loop

        print("Finished at: t={0} minutes".format(self.store3._elapsed_time))
        self.assertTrue( self.store3._elapsed_time == 6 )

    #end method

    def test_integration_4(self):
        
        while not self.store4.isEmpty():
            
            ct = self.store4.incrementTime()

            currentArrivals = self.store4.checkArrivals(ct, self.store4.customers)

            for each in self.store4.registers:
                each.checkout()
            #end loop

            whoPicks = self.store4.whoPicks(currentArrivals)

            if len(currentArrivals) > 1:

                for each in whoPicks:
                    
                    register = each.pickLine(self.store4.registers)
                    register.addCustomer(each)
                #end loop
            else:
            
                if whoPicks != False:
                
                    register = whoPicks.pickLine(self.store4.registers)
                    register.addCustomer(whoPicks)
                #end if
            #end if/else            

        #end loop

        print("Finished at: t={0} minutes".format(self.store4._elapsed_time))
        self.assertTrue( self.store4._elapsed_time == 9 )

    #end method

    def test_integration_5(self):
        
        while not self.store5.isEmpty():
            
            ct = self.store5.incrementTime()

            currentArrivals = self.store5.checkArrivals(ct, self.store5.customers)

            for each in self.store5.registers:
                each.checkout()
            #end loop

            whoPicks = self.store5.whoPicks(currentArrivals)

            if len(currentArrivals) > 1:

                for each in whoPicks:
                    
                    register = each.pickLine(self.store5.registers)
                    register.addCustomer(each)
                #end loop
            else:
            
                if whoPicks != False:
                
                    register = whoPicks.pickLine(self.store5.registers)
                    register.addCustomer(whoPicks)
                #end if
            #end if/else            

        #end loop

        print("Finished at: t={0} minutes".format(self.store5._elapsed_time))
        self.assertTrue( self.store5._elapsed_time == 11 )

    #end method

#end class

if __name__ == '__main__':
    unittest.main()