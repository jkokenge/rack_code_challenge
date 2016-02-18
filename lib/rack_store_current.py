

class GroceryStore(object):
    """Main class that controlls the other classes"""

    def __init__(self, fp):

        self._registers = []
        self._customers = []

        contents = self.getFileContents(fp)
        
        for i in range(int(contents[0])):

            if i == int(contents[0]) - 1:
                self._registers.append(TrainingCashier(i, self))
            else:
                self._registers.append(Cashier(i, self))

        del contents[0]
        
        for each in contents:
            
            type, arrived, items = tuple(each.split())
            
            try:

                c = Customer(type.strip(), arrived.strip(), items.strip())

                if type == 'A':
                    self._customers.append(TypeACustomer(c))
                elif type == 'B':
                    self._customers.append(TypeBCustomer(c))
                
            except Exception as err:
                print(err)
        # end loop
    # end constructor

    @property
    def customers(self):
        return self._customers
    @customers.setter
    def customers(self, c):
        self._customers = c
    #end property customers

    @property
    def registers(self):
        return self._registers
    @registers.setter
    def registers(self, r):
        self._registers = r
    #end property registers

    def getFileContents(self, file_path):

        with open(file_path, "r") as f:
            return f.read().splitlines()
    #end method

    def __len__(self):
        return len(self._registers)
    #end method

    def __iter__(self):
        for each in self._registers:
            yield each
    #end method


    def __repr__(self):
        return "Registers: {0}, Customers: {1}, Time Taken: {2}".format(self._registers, self._customers, self._time_taken)

# end class


class Cashier(object):
    
    def __init__(self, num, store):
        self._num = int(num)
        self._time_per_item = 1
        self._customers = []
        self._time_per_customer = []
        self._arrival_times = []
        self._store = store
    #end constructor

    def addCustomer(self, c):
        self._customers.append(c)
    #end method

    def removeCustomer(self):
        del self._customers[0]
    #end method

    def __len__(self):
        return len(self._customers)
    #end method

    def __contains__(self, cust):
        return cust in self._customers
    #end method

    def checkout(self, cust):

        time_taken = 0

        if cust == self._customers[0]:
            time_taken += cust._decorated._arrived
        else:
            pass # what to do if the current customer is NOT first in line
        
        time_taken += (cust._decorated._items * self._time_per_item)
        self._time_per_customer.append(time_taken)
        
    #end method

    def __repr__(self):
        return "Cashier number {0}, Time per Item {1}, Customers {2}, Time Per Customer {3}".format(
            self._num, self._time_per_item, self._customers, self._time_per_customer)
    #end method

#end class


class TrainingCashier(Cashier):

    def __init__(self, num, store):
        super(TrainingCashier, self).__init__(num, store)
        self._time_per_item = 2
    #end constructor

#end class


class Customer(object):

    def __init__(self, type = None, arrived = None, items = None):
        self._type = type
        self._arrived = int(arrived)
        self._items = int(items)
    #end constructor

    def pickLine(self, cashiers):
        raise NotImplementedError("Not Implemented Here!")
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

        shortest_line = self.getShortestLine()

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

    def __repr__(self):
        return "Customer type {0}, arrived at {1} minutes, with {2} items".format(self._type, self._arrived, self._items)

#end class

class TypeACustomer(object):

    def __init__(self, decorated = None):
        self._decorated = decorated
    #end constructor

    def pickLine(self, cashiers):
        
        if len(cashiers) == 1:  # if only 1 cashier
            cashiers[0].addCustomer(self)
            return cashiers[0]
        else:
            
            shortest = self._decorated.getShortestLine()
            shortest.addCustomer(self)
            return shortest
    #end method

    def __repr__(self):
        return "Customer type {0}, arrived at {1} minutes, with {2} items".format(self._decorated._type, self._decorated._arrived, self._decorated._items)

#end class


class TypeBCustomer(object):

    def __init__(self, decorated = None):
        self._decorated = decorated
    #end constructor

    def pickLine(self, cashiers):
        
        if len(cashiers) == 1:  # if only 1 cashier
            cashiers[0].addCustomer(self)
            return cashires[0]
        else:
            
            least_items = self._decorated.getLineWithLeastItems(cashiers)
            least_items.addCustomer(self)
            return least_items
    #end method

    def __repr__(self):
        return "Customer type {0}, arrived at {1} minutes, with {2} items".format(self._decorated._type, self._decorated._arrived, self._decorated._items)

#end class


def main():
    str1 = GroceryStore("inputFiles/ex1.txt")
    print(str1)

if __name__ == "__main__":
    main()