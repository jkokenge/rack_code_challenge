import unittest
import sys

sys.path.append("C:\\bin\\rack_code_challenge\\lib")
from rack_store import *


class test_customers(unittest.TestCase):

    def setUp(self):

        self.store = GroceryStore("inputFiles/ex1.txt")
        self.store2 = GroceryStore("inputFiles/ex2.txt")

    def test_customer_type_input1(self):
        
        for each in self.store._customers:
            self.assertTrue( each._decorated._type == 'A' )
    #end method

    def test_registers_input1(self):

        self.assertTrue( len(self.store._registers) == 1 )
        self.assertTrue( isinstance(self.store._registers[0], TrainingCashier) )
    #end method

    def test_customer_behavior_input1(self):

        self.assertTrue( len(self.store._customers) == 2 )
        self.assertTrue( type(self.store._customers) == list )
        self.assertTrue( type(self.store._registers) == list )

        for each in self.store._customers:
            each.pickLine(self.store._registers)
        #end loop

        cust = list(self.store._customers)

        for each in self.store._customers:
            self.assertTrue( each in cust )

        #print("store registers after getting customers", self.store._registers[0])
    #end method

    def test_checkout_times_input1(self):

        for each in self.store._customers:
            each.pickLine(self.store._registers)
        #end loop

        self.assertTrue(self.store._registers[0]._time_per_item == 2)

        reg = self.store._registers[0]
        #print("register", reg)
        time_taken = reg.checkout()
        print("*** time_taken scenario 1:", time_taken)
        self.assertTrue( time_taken == 7 )
    #end method


    ####### testing input file 2 begins here #######

    def test_customer_type_input2(self):
        
        custs = self.store2._customers

        for index, each in enumerate(custs):
            
            if index % 2 == 0:
                self.assertTrue( each._decorated._type == 'A' )
            else:
                self.assertTrue( each._decorated._type == 'B' )

    #end method

    def test_registers_input2(self):

        self.assertTrue( len(self.store2._registers) == 2 )
        self.assertTrue( isinstance(self.store2._registers[1], TrainingCashier) )
    #end method

    def test_customer_behavior_input2(self):

        self.assertTrue( len(self.store2._customers) == 5 )
        self.assertTrue( type(self.store2._customers) == list )
        self.assertTrue( type(self.store2._registers) == list )

        for each in self.store2._customers:
            each.pickLine(self.store2._registers)
        #end loop

        cust = list(self.store2._customers)

        for each in self.store2._customers:
            self.assertTrue( each in cust )

        #print("store registers after getting customers", self.store2._registers)
    #end method

    def test_checkout_times_input2(self):

        for each in self.store2._customers:
            each.pickLine(self.store2._registers)
        #end loop

        #print(self.store2._registers)
        self.assertTrue(self.store2._registers[1]._time_per_item == 2)

        time_taken = 0
        reg = self.store2._registers
        
        for each in reg:
            time_taken += each.checkout()
        print("*** time_taken scenario 2", time_taken)
        self.assertTrue( time_taken == 13 )
    #end method

if __name__ == '__main__':
    unittest.main()
