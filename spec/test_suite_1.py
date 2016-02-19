import unittest
import sys

sys.path.append("C:\\bin\\rack_code_challenge\\lib")
from rack_store_1 import *


class test_customers(unittest.TestCase):

    def setUp(self):

        self.store = GroceryStore("inputFiles/ex1.txt")
        self.store2 = GroceryStore("inputFiles/ex2.txt")
        self.store3 = GroceryStore("inputFiles/ex3.txt")
        self.store4 = GroceryStore("inputFiles/ex4.txt")
        self.store5 = GroceryStore("inputFiles/ex5.txt")

    def test_customer_type_input1(self):
        
        for each in self.store._customers:
            self.assertTrue( each._decorated._type == 'A' )
    #end method

    def test_registers_input1(self):

        self.assertTrue( len(self.store._registers) == 1 )
        self.assertTrue( isinstance(self.store._registers[-1], TrainingCashier) )
    #end method

    def test_customer_behavior_input1(self):

        self.assertTrue( len(self.store._customers) == 2 )
        self.assertTrue( type(self.store._customers) == list )
        self.assertTrue( type(self.store._registers) == list )
        self.assertTrue(self.store._registers[-1]._time_per_item == 2)

        for each in self.store._customers:
            
            register = each.pickLine(self.store._registers)
            self.assertTrue(each in register)
        #end loop

    #end method

    def test_checkout_times_input1(self):

        for index, each in enumerate(self.store._customers):
            
            if not index == 0:
                self.store.checkArrivalTime(each)
            register = each.pickLine(self.store._registers)
            register.checkout(each)
        #end loop

        #for each in self.store:
        #    print(each)
        
        #print("*** input 1's time taken was {0} and it should have been 7 ***".format(
        #    self.store.calculateTimes()))
        self.assertTrue( self.store.calculateTimes() == 7 )

    #end method


    ######## testing input file 2 begins here #######


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
        self.assertTrue( isinstance(self.store2._registers[-1], TrainingCashier) )
    #end method

    def test_customer_behavior_input2(self):

        self.assertTrue( len(self.store2._customers) == 5 )
        self.assertTrue( type(self.store2._customers) == list )
        self.assertTrue( type(self.store2._registers) == list )
        self.assertTrue(self.store._registers[-1]._time_per_item == 2)

        for each in self.store2._customers:
            register = each.pickLine(self.store2._registers)
            self.assertTrue(each in register)
        #end loop

    #end method

    def test_customer_behavior2_input2(self):

        for index, each in enumerate(self.store2._customers):
            
            if index != 0:
                self.store2.checkArrivalTime(each)
            #end if

            register = each.pickLine(self.store2._registers)

            if index == 0:
                self.assertTrue(self.store2._customers[0] in self.store2._registers[0])
            elif index == 1:
                self.assertTrue(self.store2._customers[1] in self.store2._registers[1])
            elif index == 2:
                self.assertTrue(self.store2._customers[2] in self.store2._registers[0])
            elif index == 3:
                self.assertTrue(self.store2._customers[3] in self.store2._registers[1])
            elif index == 4:
                self.assertTrue(self.store2._customers[4] in self.store2._registers[0])

            register.checkout(each)
    #end method

    def test_checkout_times_input2(self):

        for index, each in enumerate(self.store2._customers):

            if not index == 0:
                self.store2.checkArrivalTime(each)
            register = each.pickLine(self.store2._registers)
            register.checkout(each)

            #x = raw_input("")
            #print("customer {0} arrived after {1} minutes carrying {2} items".format(
            #    index+1, each._decorated._arrived, each._decorated._items))
            #print("")
            #for i in self.store2:
            #    print(i)
            #end loop

        #end loop

        #x = raw_input("at the end")
        #print("\nTHE END\n\n")
        #for each in self.store2:
        #    print(each)

        #print("*** input 2's time taken was {0} and it should have been 13 ***".format(
        #    self.store2.calculateTimes()))
        self.assertTrue( self.store2.calculateTimes() == 13 )

    #end method


    ######## testing input file 3 begins here #######

    def test_customer_type_input3(self):
        
        for each in self.store3._customers:
            self.assertTrue( each._decorated._type == 'A' )
    #end method

    def test_registers_input3(self):

        self.assertTrue( len(self.store3._registers) == 2 )
        self.assertTrue( isinstance(self.store3._registers[-1], TrainingCashier) )
    #end method

    def test_customer_behavior_input3(self):

        self.assertTrue( len(self.store3._customers) == 4 )
        self.assertTrue( type(self.store3._customers) == list )
        self.assertTrue( type(self.store3._registers) == list )
        self.assertTrue(self.store3._registers[-1]._time_per_item == 2)

        for each in self.store3._customers:
            register = each.pickLine(self.store3._registers)
            self.assertTrue(each in register)
        #end loop

        #print("store registers after getting customers", self.store._registers[0])
    #end method

    def test_checkout_times_input3(self):

        for index, each in enumerate(self.store3._customers):

            if not index == 0:
                self.store3.checkArrivalTime(each)
            register = each.pickLine(self.store3._registers)
            register.checkout(each)

            #x = raw_input("")
            #print("customer {0} arrived after {1} minutes carrying {2} items".format(
            #    index+1, each._decorated._arrived, each._decorated._items))
            #print("")
            #for i in self.store3:
            #    print(i)
            #end loop

        #end loop

        print("*** input 3's time taken was {0} and it should have been 6 ***".format(
            self.store3.calculateTimes()))
        self.assertTrue( self.store3.calculateTimes() == 6 )

    #end method


    ######## testing input file 4 begins here #######


    def test_customer_type_input4(self):
        
        custs = self.store4._customers

        for each in custs:
            self.assertTrue( each._decorated._type == 'A' )

    #end method

    def test_registers_input4(self):

        self.assertTrue( len(self.store4._registers) == 2 )
        self.assertTrue( isinstance(self.store4._registers[-1], TrainingCashier) )
    #end method

    def test_customer_behavior_input4(self):

        self.assertTrue( len(self.store4._customers) == 4 )
        self.assertTrue( type(self.store4._customers) == list )
        self.assertTrue( type(self.store4._registers) == list )
        self.assertTrue(self.store._registers[-1]._time_per_item == 2)

        for each in self.store4._customers:
            register = each.pickLine(self.store4._registers)
            self.assertTrue(each in register)
        #end loop

    #end method

    def test_checkout_times_input4(self):

        for index, each in enumerate(self.store4._customers):

            if not index == 0:
                self.store4.checkArrivalTime(each)
            register = each.pickLine(self.store4._registers)
            register.checkout(each)

            #x = raw_input("")
            #print("customer {0} arrived after {1} minutes carrying {2} items".format(
            #    index+1, each._decorated._arrived, each._decorated._items))
            #print("")
            #for i in self.store4:
            #    print(i)
            #end loop

        #end loop

        #x = raw_input("at the end")
        #print("\nTHE END\n\n")
        #for each in self.store4:
        #    print(each)

        #print("*** input 4's time taken was {0} and it should have been 9 ***".format(
        #    self.store4.calculateTimes()))
        self.assertTrue( self.store4.calculateTimes() == 9 )

    #end method


    ######## testing input file 5 begins here #######


    def test_customer_type_input5(self):
        
        custs = self.store5._customers

        for index, each in enumerate(custs):

            if index ==3:
                self.assertTrue( each._decorated._type == 'B' )
            else:
                self.assertTrue( each._decorated._type == 'A' )

    #end method

    def test_registers_input5(self):

        self.assertTrue( len(self.store5._registers) == 2 )
        self.assertTrue( isinstance(self.store5._registers[-1], TrainingCashier) )
    #end method

    def test_customer_behavior_input5(self):

        self.assertTrue( len(self.store5._customers) == 5 )
        self.assertTrue( type(self.store5._customers) == list )
        self.assertTrue( type(self.store5._registers) == list )
        self.assertTrue(self.store._registers[-1]._time_per_item == 2)

        for each in self.store5._customers:
            register = each.pickLine(self.store5._registers)
            self.assertTrue(each in register)
        #end loop

    #end method

    def test_checkout_times_input5(self):

        for index, each in enumerate(self.store5._customers):

            if not index == 0:
                self.store5.checkArrivalTime(each)
            register = each.pickLine(self.store5._registers)
            register.checkout(each)

            #x = raw_input("")
            #print("customer {0} arrived after {1} minutes carrying {2} items".format(
            #    index+1, each._decorated._arrived, each._decorated._items))
            #print("")
            #for i in self.store5:
            #    print(i)
            #end loop

        #end loop

        #x = raw_input("at the end")
        #print("\nTHE END\n\n")
        #for each in self.store5:
        #    print(each)

        print("*** input 5's time taken was {0} and it should have been 11 ***".format(
            self.store5.calculateTimes()))
        self.assertTrue( self.store5.calculateTimes() == 11 )

    #end method

if __name__ == '__main__':
    unittest.main()
