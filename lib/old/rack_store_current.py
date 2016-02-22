

class Helper(object):

    @staticmethod
    def getFileContents(file_path):

        with open(file_path, "r") as f:
            return f.read().splitlines()
    #end method

    @staticmethod
    def customerType(type, arrived, items):

        if type == 'A':
            return TypeACustomer(type, arrived, items)
        elif type == 'B':
            return TypeBCustomer(type, arrived, items)

    #end method

#end class


class GroceryStore(object):
    
    def __init__(self, lst):
        
        self._registers = []
        self._customers = []
        self._elapsed_time = 0
        
        for i in range(int(lst[0])):

            if i == int(lst[0]) - 1:
                self._registers.append(TrainingCashier(i, self))
            else:
                self._registers.append(Cashier(i, self))

        del lst[0]
        
        for each in lst:            
            type, arrived, items = tuple(each.split())
            self._customers.append(Helper.customerType(type, arrived, items))
        # end loop

    # end constructor
    
    def increment_time(self):
        self._elapsed_time += 1
        return self._elapsed_time
    #end method    

    def checkArrivals(self, timeVal):

        comeIn = []

        for each in self._customers:

            if timeVal == each._arrived:
                comeIn.append(each)
            #end if
        #end loop

        return comeIn
    #end method

    def whoPicks(self, custList = []):
        
        if len(custList) == 1:
            return custList[0]
        elif len(custList) > 1:
            
            itemSort = sorted(custList, key = lambda each: each._items)
            #print("itemSort {0}".format(itemSort))
            if itemSort[0]._items == itemSort[1]._items:
                typeSort = sorted(custList, key = lambda each: each._type)
                return typeSort[0]
            #end if

            return itemSort[0]

    #end method

    def noCustomers(self):

        empties = []
        for each in self:
            if each.isEmpty():
                empties.append(True)
            else:
                empties.append(False)
        #end loop
        return False if False in empties else True
    #end method

    def __len__(self):
        return len(self._registers)
    #end method

    def __iter__(self):
        for each in self._registers:
            yield each
    #end method

    def __repr__(self):
        return "Registers: \n\t{0} \nCustomers: \n\t{1} \nElapsed Time: \n\t{2}".format(
            self._registers, self._customers, self._elapsed_time)
    #end method

#end class


class Cashier(object):
    
    def __init__(self, num, store):
        self._num = int(num)
        self._time_per_item = 1
        self._customers = []
        self._time_per_customer = []
        self._arrival_times = []
        self._store = store
        self._isEmpty = True
    #end constructor

    def addCustomer(self, c):
        self._customers.append(c)
    #end method

    def removeCustomer(self):
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

    def calculateLeave(self, cust):
        
        time_left = 0
        arrived = cust._arrived

        if self.isFirstHere(cust): # if it's the first customer in line, include arrival time
            time_left += arrived
            time_left += ( cust._items * self._time_per_item )
            
        else:
            
            last_customer_left = self._time_per_customer[-1]
            
            if arrived < last_customer_left: # if they arrived before last customer left
                time_left += last_customer_left
                time_left += ( cust._items * self._time_per_item )
                
            else: # if they arrived after last customer left
                time_left += (arrived - last_customer_left) + ( cust._items * self._time_per_item )
            #end if else
        #end if else

        self._time_per_customer.append(time_left)
        return time_left

    #end method

    def isFirstHere(self, cust):
        
        num_registers = len(self._store)

        for index, each in enumerate(self._store._customers):

            if index < num_registers:
                if cust == each:
                    return True
            #end if
        #end loop

        return False

    #end method

    def checkout(self):
        
        #time_left = self.calculateLeave(cust)

        first_customer = self._customers[0]
        print("FIRST CUSTOMER {0} id is {1}".format(first_customer, id(first_customer)))
        if first_customer is None:
            return

        if isinstance(self, TrainingCashier):
            first_customer._items -= 0.5
        elif isinstance(self, Cashier):
            first_customer._items -= 1

        if first_customer._items == 0:
            print("CUSTOMER LEAVING {}".format(first_customer))
            self.calculateLeave(first_customer)
            self.removeCustomer()
            
        #end if

        #return time_left
        
    #end method

    def __repr__(self):
        return "Cashier number {0}, Time per Item {1}, Customers {2}, Time Per Customer {3}".format(
            self._num+1, self._time_per_item, self._customers, self._time_per_customer)
    #end method

#end class


class TrainingCashier(Cashier):

    def __init__(self, num, store):
        self._num = int(num)
        self._time_per_item = 2
        self._customers = []
        self._time_per_customer = []
        self._arrival_times = []
        self._store = store
        self._isEmpty = True
    #end constructor

#end class


class Customer(object):

    def __init__(self, type = None, arrived = None, items = None):
        self._type = type
        self._arrived = int(arrived)
        self._items = int(items)
    #end constructor

    def pickLine(self, cashiers):
        raise NotImplementedError("Implemented in Subclasses")
    #end method

    def getShortestLine(self, cashiers):

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

    def compareItems(self, other):
        return 1 if self._items > other._items else 0
    #end method

    def compareType(self, other):
        return 1 if self._type > other._type else 0
    #end method

    def __eq__(self, other):
        return 1 if self._type == other._type and self._arrived == other._arrived \
            and self._items == other._items else 0
    #end method

    def __len__(self):
        return len(self._items)
    #end method

    def __repr__(self):
        return "Customer type {0}, arrived at {1} minutes, with {2} items".format(self._type, self._arrived, self._items)

#end class


class TypeACustomer(Customer):

    def __init__(self, type = None, arrived = None, items = None):
        return super(TypeACustomer, self).__init__(type, arrived, items)
    #end constructor

    def pickLine(self, cashiers):
        
        if len(cashiers) == 1:  # if only 1 cashier
            cashiers[0].addCustomer(self)
            return cashiers[0]
        else:
            
            shortest = self.getShortestLine(cashiers)
            shortest.addCustomer(self)
            return shortest
    #end method

#end class


class TypeBCustomer(Customer):

    def __init__(self, type = None, arrived = None, items = None):
        return super(TypeBCustomer, self).__init__(type, arrived, items)
    #end constructor

    def pickLine(self, cashiers):
        
        if len(cashiers) == 1:  # if only 1 cashier
            cashiers[0].addCustomer(self)
            return cashires[0]
        else:
            
            least_items = self.getLineWithLeastItems(cashiers)
            least_items.addCustomer(self)
            return least_items
    #end method

#end class