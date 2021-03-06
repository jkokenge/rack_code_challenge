""" 
Table Of Contents:
    1. Helper
    2. GroceryStore
    3. Customer
    4. TypeACustomer
    5. TypeBCustomer
    5. Cashier
    6. TrainingCashier
"""
import os

class Helper(object):

    """ !1. Helper Methods
            a.) getFileContents : takes filePath and returns a list of the contents
            b.) customerType : takes a tuple of customer information and returns correct
                customer type
            c.) getRegisters : takes an int and returns a list of Cashiers with the
                last one being a training Cashier"""

    @staticmethod
    def getFileContents(file_path):

        """ @param file_path : String
            @return list """

        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                return f.read().splitlines()
        else:
            raise IOError("Not a valid File")
    #end method

    @staticmethod
    def customerType(type, arrived, items):

        """ @param type: String
            @param arrived: int
            @param items: int
            @return TypeACustomer or TypeBCustomer """

        if type == 'A':
            return TypeACustomer(type, arrived, items)
        elif type == 'B':
            return TypeBCustomer(type, arrived, items)

    #end method

    @staticmethod
    def getRegisters(item, store):

        """ @param item : int
            @param store : GroceryStore
            @return list of Cashier"""
        
        registers = []
        for i in range(item):

            if i == int(item) - 1:
                registers.append(TrainingCashier(i, store))
            else:
                registers.append(Cashier(i, store))
            #end if
        #end loop
        return registers
    #end method

#end class


class GroceryStore(object):

    """ !2.) GroceryStore Methods 
            a.) __init__ : takes list of Cashiers and list of Customers
            b.) checkArrivals : takes a timeValue and a list of Customers
                and returns a list of Customers who are getting in line
            c.) whoPicks : takes a list of Customers who are to get in line
                and checks the number of items and type of customer
                to determine which customer gets in line first 
            d.) incrementTime: increments the elapsed time by 1 minute """

    def __init__(self, registers = [], customers = []):
        self._registers = registers
        self._customers = customers
        self._elapsed_time = 0
    #end constructor

    @property
    def registers(self):
        return self._registers
    @registers.setter
    def registers(self, regs = []):
        self._registers = regs
    #end property registers

    @property
    def customers(self):
        return self._customers
    @customers.setter
    def customers(self, custs = []):
        self._customers = custs
    #end property customers

    def isEmpty(self):
        return True if len(self.customers) == 0 else False
    #end method

    def checkArrivals(self, timeVal = 1, custList = []):

        """ @param timeVal : int
            @param custList : list of Customer 
            @return comeIn : list of Customer """

        comeIn = []

        for each in custList:

            if timeVal == each._arrived:
                comeIn.append(each)
            #end if
        #end loop

        return comeIn
    #end method

    def whoPicks(self, custList = []):

        """ @param custList: list
            @return Customer or False """
        
        if len(custList) == 1:
            return custList[0]
        elif len(custList) > 1:
            
            itemSort = sorted(custList, key = lambda each: each._items)
            
            if itemSort[0]._items == itemSort[1]._items:
                typeSort = sorted(custList, key = lambda each: each._type)
                return typeSort
            #end if

            return itemSort
        else:
            return False

    #end method

    def incrementTime(self):
        self._elapsed_time += 1
        return self._elapsed_time
    #end method

    def __len__(self):
        return len(self._registers)
    #end method

    def __iter__(self):
        for each in self._registers:
            yield each
    #end method

    def __repr__(self):
        return "Registers: \n\t{0} \n\nCustomers: \n\t{1} \n\nElapsed Time: \n\t{2}".format(
            self._registers, self._customers, self._elapsed_time)
    #end method

#end class


class Customer(object):

    """ !3.) Customer Methods
            a.) __init__ : takes a type, an arrival time, and a number of items
            b.) pickLine : not implemented here but will vary depending on
                customer type
            c.) getShortestLine : takes a list of Cashiers and returns the line
                with the fewest customers in it
            d.) getLineWithLeastItems : takes a list of Cashiers and returns the
                line where the last customer has the fewest items """

    def __init__(self, type = None, arrived = None, items = None):
        self._type = type
        self._arrived = int(arrived)
        self._items = int(items)
    #end constructor

    def pickLine(self, cashiers):
        raise NotImplementedError("Implemented in Subclasses")
    #end method

    def getShortestLine(self, cashiers):

        """ @param cashiers : list
            @return shortest : Cashier """

        if len(cashiers) == 1:  # there is only 1 line to get in
            shortest = cashiers[0]
        else:
            for index, each in enumerate(cashiers):

                if index == 0:  # set the first line as the shortest for now
                    shortest = each
                else:
                    if len(shortest._customers) > len(each._customers):     # if current is shorter
                        shortest = each
            #end loop
        #end if else

        return shortest
    #end method

    def getLineWithLeastItems(self, cashiers):

        """ @param cashiers : list of Cashier
            @return least_items : Cashier """

        shortest_line = self.getShortestLine(cashiers)

        if shortest_line.isEmpty():
            least_items = shortest_line
        else:
            for index, each in enumerate(cashiers):

                if index == 0:
                    least_items = each
                else:

                    if least_items._customers[-1]._items > each._customers[-1]._items:
                        least_items = each
                #end if else
            #end loop
        #end if else

        return least_items
    #end method

    #def __eq__(self, other):
    #    return True if self._type == other._type and self._arrived == other._arrived \
    #        and self._items == other._items else False
    ##end method

    def __len__(self):
        return self._items
    #end method

    def __repr__(self):
        return "Customer type {0}, arrived at {1} minutes, with {2} items remaining".format(
            self._type, self._arrived, self._items)

#end class


class TypeACustomer(Customer):

    def __init__(self, type = None, arrived = None, items = None):
        return super(TypeACustomer, self).__init__(type, arrived, items)
    #end constructor

    def pickLine(self, cashiers):

        """ @param cashiers: list of Cashier
            @return shortest : Cashier """
        
        if len(cashiers) == 1:  # if only 1 cashier
            return cashiers[0]
        else:
            
            shortest = self.getShortestLine(cashiers)
            return shortest
    #end method

#end class


class TypeBCustomer(Customer):

    def __init__(self, type = None, arrived = None, items = None):
        return super(TypeBCustomer, self).__init__(type, arrived, items)
    #end constructor

    def pickLine(self, cashiers):

        """ @param cashiers: list of Cashier
            @return least_items: Cashier """
        
        if len(cashiers) == 1:  # if only 1 cashier
            return cashires[0]
        else:
            
            least_items = self.getLineWithLeastItems(cashiers)
            return least_items
    #end method

#end class


class Cashier(object):

    """ !5. Cashier Methods
            a.) __init__ : takes an index and a GroceryStore
            b.) addCustomer : adds a customer to the line
            c.) removeCustomer : removes the customer from the store and the line
                after adding when that customer left to the _time_per_customer list
            d.) isEmpty : checks if this line has customers or not
            e.) checkout : calculates if an item has been processed 
                and removes the current customer if they have no items left """
    
    def __init__(self, num, store):
        self._num = int(num)
        self._store = store
        self._time_per_item = 1
        self._customers = []
        self._time_per_customer = []
        self._arrival_times = []
        self._isEmpty = True
    #end constructor

    def addCustomer(self, c):

        """ @param c : Customer """

        self._customers.append(c)
    #end method

    def removeCustomer(self):
        self._time_per_customer.append(self._store._elapsed_time)
        self._store._customers.remove(self._customers[0])
        del self._customers[0]
    #end method

    def isEmpty(self):
        return True if len(self) == 0 else False
    #end method

    def __len__(self):
        return len(self._customers)
    #end method

    def __contains__(self, cust):
        return cust in self._customers
    #end method

    def checkout(self):

        if len(self) == 0:
            return

        first_customer = self._customers[0]
        current_time = self._store._elapsed_time
        remove_item = False
        
        #if the first customer in line did NOT just arrive
        if current_time != first_customer._arrived:

            #if a customer has already come and gone
            if len(self._time_per_customer) > 0:
                
                time_since_last_left = current_time - self._time_per_customer[-1]

                if time_since_last_left % self._time_per_item == 0:
                    remove_item = True

            else:

                time_since_arrival = current_time - first_customer._arrived

                if time_since_arrival % self._time_per_item == 0:
                    remove_item = True
                #end if
            #end if/else

            if remove_item:    
                first_customer._items -= 1

                if first_customer._items == 0:
                    self.removeCustomer()
                #end if
        
    #end method

    def __repr__(self):
        return "Cashier number {0}, Time per Item {1}, Customers {2}".format(
            self._num+1, self._time_per_item, self._customers)
    #end method

#end class


class TrainingCashier(Cashier):

    def __init__(self, num, store):
        super(TrainingCashier, self).__init__(num, store)
        self._time_per_item = 2
    #end constructor    

#end class