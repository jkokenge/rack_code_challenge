

class GroceryStore(object):
    """Main class that controlls the other classes"""

    def __init__(self, fp):

        self._registers = []
        self._customers = []
        self._time_taken = 0

        contents = self.getFileContents(fp)
        
        for i in range(int(contents[0])):

            if i == int(contents[0]) - 1:
                self._registers.append(TrainingCashier(i))
            else:
                self._registers.append(Cashier(i))

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

    @property
    def time_taken(self):
        return self._time_taken
    @time_taken.setter
    def time_taken(self, t):
        self._time_taken = t
    #end property time_taken

    def getFileContents(self, file_path):

        with open(file_path, "r") as f:
            return f.read().splitlines()
    #end method

    def __repr__(self):
        return "Registers: {0}, Customers: {1}, Time Taken: {2}".format(self._registers, self._customers, self._time_taken)

# end class


class Cashier(object):
    
    def __init__(self, num):
        self._num = int(num)
        self._time_per_item = 1
        self._customers = []
    #end constructor

    def reportTime(self):
        pass

    def addCustomer(self, c):
        self._customers.append(c)
    #end method

    def removeCustomer(self):
        del self._customers[0]
    #end method

    def checkout(self):

        time_taken = 0

        for index, each in enumerate(self._customers):
            #print("customer", each)

            if index == 0:
                time_taken += each._decorated._arrived
            else:
                time_taken += each._decorated._arrived if each._decorated._arrived > time_taken else 0
            
            #print("time_taken while in loop", time_taken, "customer #", index)
            time_taken += (each._decorated._items * self._time_per_item)
            
            #print("time_taken while in loop", time_taken, "customer #", index)
        #end loop

        self._customers = []

        return time_taken
    #end method

    def __repr__(self):
        return "Cashier number {0}, Time per Item {1}, Customers {2}".format(self._num, self._time_per_item, self._customers)


#end class


class TrainingCashier(Cashier):

    def __init__(self, num):
        self._num = int(num)
        self._time_per_item = 2
        self._customers = []
    #end constructor

    def __repr__(self):
        return super(TrainingCashier, self).__repr__()

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

    def __repr__(self):
        return "Customer type {0}, arrived at {1} minutes, with {2} items".format(self._type, self._arrived, self._items)

#end class

class TypeACustomer(object):

    def __init__(self, decorated = None):
        self._decorated = decorated
    #end constructor

    def pickLine(self, cashiers):
        
        if len(cashiers) == 1:
            cashiers[0].addCustomer(self)
        else:
            
            for index, each in enumerate(cashiers):
                if index == 0:
                    shortest = each
                elif len(each._customers) < shortest:
                    shortest = each
            #end loop

            each.addCustomer(self)
    #end method

    def __repr__(self):
        return "Customer type {0}, arrived at {1} minutes, with {2} items".format(self._decorated._type, self._decorated._arrived, self._decorated._items)

#end class


class TypeBCustomer(object):

    def __init__(self, decorated = None):
        self._decorated = decorated
    #end constructor

    def pickLine(self, cashiers):
        
        least_items = self.pick_shortest_line(cashiers)
        print("least_items", least_items)
        least_items.addCustomer(self)

    #end method

    def pick_shortest_line(self, cashiers):
        #print("ALL CASHIERS", cashiers)
        if len(cashiers) == 1:
            return cashiers[0]
        else:

            for index, each in enumerate(cashiers):
                print(each)
                customers = each._customers
                #print("index of cashiers", index, "customers", customers)
                if len(customers) == 0:
                    least_items = each
                    break   
                else:
                    if index == 0:
                        least_items = each
                    else:
                        if least_items._customers[-1]._decorated._items < customers[-1]._decorated._items:
                            least_items = each  
                        
            #end loop

            return least_items

    def __repr__(self):
        return "Customer type {0}, arrived at {1} minutes, with {2} items".format(self._decorated._type, self._decorated._arrived, self._decorated._items)

#end class


def main():
    str1 = GroceryStore("inputFiles/ex1.txt")
    print(str1)

if __name__ == "__main__":
    main()