import unittest
import sys

sys.path.append("C:\\bin\\rack_code_challenge\\lib")
from store import *


class test_customers(unittest.TestCase):

    def setUp(self):

        lst1 = Helper.getFileContents("inputFiles/ex1.txt")
        #lst2 = Helper.getFileContents("inputFiles/ex2.txt")

        registers = Helper.getRegisters(lst1[0])
        del lst1[0]

        custs = []

        for each in lst1:
            type, arrived, items = tuple(each.split())
            custs.append(Helper.customerType(type, arrived, items))
        #end loop

        self.store1 = GroceryStore(registers, custs)
        #self.store2 = GroceryStore(lst2)

    #end set up method

    

#end class

if __name__ == '__main__':
    unittest.main()