import unittest
import sys

sys.path.append("C:\\bin\\rack_code_challenge\\lib")
from rack_store_current import *


class test_customers(unittest.TestCase):

    def setUp(self):

        lst1 = Helper.getFileContents("inputFiles/ex1.txt")
        lst2 = Helper.getFileContents("inputFiles/ex2.txt")
        self.store1 = GroceryStore(lst1)
        self.store2 = GroceryStore(lst2)

    #end set up method

    def test_types(self):

        for each in self.store1._customers:
            self.assertTrue(each._type == 'A')
        #end loop

        self.assertTrue(len(self.store1) == 1)
    #end method

    #def test_input1_p1(self):
        
    #    for each in self.store1._customers:

    #        currentTime = self.store1.increment_time()
    #        arrivals = self.store1.checkArrivals(currentTime)
    #        #print(arrivals)
    #        cust = self.store1.whoPicks(arrivals)
    #        #print(cust)

    #        register = cust.pickLine(self.store1._registers)
    #        #print(register)
    #        time_left = register.checkout(each)
    #        #print(time_left)
    #    #end loop
        
    ##end method

    def test_input2_p1(self):

        #print(len(self.store2._customers))
        #print(self.store2._customers)
        #self.store2._customers.remove(self.store2._customers[0])
        ##del self.store2._customers[0]
        #print(len(self.store2._customers))
        #print(self.store2._customers)
        
        while True:

            currentTime = self.store2.increment_time()
            print("time elapsed is {}\n".format(currentTime))
            x = raw_input("")
            arrivals = self.store2.checkArrivals(currentTime)                
            
            try:
                cust = self.store2.whoPicks(arrivals)
            
                register = cust.pickLine(self.store2._registers)
                #print(register)
                #time_left = register.checkout(cust)
                #print("cust left after {} minutes".format(time_left))
                for each in self.store2:
                    each.checkout()
            except Exception as err:
                #print(self.store2)
                print("customers remaining in store {}".format(len(self.store2._customers)))
                
            #print(self.store2)
            
        #end loop
        

        #print(self.store2)
        
    #end method

#end class

if __name__ == '__main__':
    unittest.main()