

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

    def checkArrivalTime(self, cust):
        
        arrived = cust._decorated._arrived

        for index, each in enumerate(self): # each is a register here
            
            if len(each) == 0:
                continue
            #end if
            
            current_first_customer = each._customers[0]
            first_customer_time_taken = each._time_per_customer[0]
            first_customer_arrived = each._arrival_times[0]
            
            # if the first customer in this line's arrival time, doesn't match the arrival
            # time of the first customer to arrive in this line
            if current_first_customer._decorated._arrived != first_customer_arrived: 
                continue
            
            if arrived > first_customer_time_taken + first_customer_arrived:
                each.removeCustomer()
                #print("customer arrived after {0} minutes at register {1} first \
                #customer in line took {2} minutes".format(
                #    arrived, index+1, first_customer_time_taken))
            #end if

        #end loop

    #end method

    def calculateTimes(self):

        if len(self) == 1:
            #return sum(self._registers[0]._time_per_customer)
            val =[]
            for each in self: # each is a register here
                #print("***************** {0}".format(each._arrival_times))
                for i, v in enumerate(each._time_per_customer):
                    
                    if i == 0:
                        val.append( each._arrival_times[i] + each._time_per_customer[i] )
                    else:
                        val.append( v )
                #end loop
            #end loop
            return sum(val)
        else:

            times = []

            for each in self: # each is a register here
                print("arrival times {0} time per customer {1}".format(each._arrival_times, each._time_per_customer))
                print("")
                val = []
                for i, v in enumerate(each._time_per_customer):
                    
                    if i == 0:
                        val.append( each._arrival_times[i] + each._time_per_customer[i] )
                    else:
                        val.append( v )
                #end loop
                #print("total time for this register is {}".format(val))
                times.append(sum(val))

            #end loop

            return max(times)
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
        self._isEmpty = True
    #end constructor

    def addCustomer(self, c):
        self._customers.append(c)
    #end method

    def removeCustomer(self):
        del self._customers[0]
    #end method

    def isEmpty(self):
        return True if len(self._customers) == 0 else False
    #end method

    def __len__(self):
        return len(self._customers)
    #end method

    def __contains__(self, cust):
        return cust in self._customers
    #end method

    def checkout(self, cust):

        time_taken = 0        
        time_taken += int(cust._decorated._items * self._time_per_item)

        #if cust == self._store._customers[0]:
        #    time_taken += int(cust._decorated._arrived)
        #end if

        self._arrival_times.append(cust._decorated._arrived)
        self._time_per_customer.append(time_taken)
        
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

        shortest_line = self.getShortestLine(cashiers)

        if shortest_line.isEmpty():
            least_items = shortest_line
        else:
            for index, each in enumerate(cashiers):

                if index == 0:
                    least_items = each
                else:

                    if least_items._customers[-1]._decorated._items > each._customers[-1]._decorated._items:
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
            
            shortest = self._decorated.getShortestLine(cashiers)
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