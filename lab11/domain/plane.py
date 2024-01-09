from domain.passenger import Passenger


class Plane:
    '''
    Descr: contains the initial, string representation, setters, getters
    and different functions and features for a plane
    '''

    def __init__(self,number,company,seats,destination,list_passengers):
        '''
        Descr: initializes the attributes of a plane in the class
        Precondition: number,seats- numbers, company, destination- strings, list_passengers- list
        Input: (self),number,seats, company, destination, list_passengers
        '''

        if number<0:
            self.__number=-1
        else:
            self.__number=number

        if len(company)<1:
            self.__company=""
        else:
            self.__company=company

        if seats<1:
            self.__seats=0
        else:
            self.__seats=seats

        if len(destination)<1:
            self.__destination=""
        else:
            self.__destination=destination

        self.__passengers=list_passengers

    '''
    Descr: each getter function returns an attribute of a plane predefined in the class
    Input: the class itself
    Output: number,seats, company, destination, list_passengers- accessed through the corresponding initial value defined in the class for each function
    '''
    def number_getter(self):
        return self.__number

    def company_getter(self):
        return self.__company

    def seats_getter(self):
        return self.__seats

    def destination_getter(self):
        return self.__destination

    def passengers_getter(self):
        return self.__passengers

    # 6
    def passengers_getter_special(self,string):
        lst=list(filter(lambda x: x.first_starts_with_string(string),self.__passengers))
        return len(lst)

    '''
        Descr: each setter function changes a specific attribute of a plane, predefined variables in the class, with new 
        values
        Precondition: number,seats- numbers, company, destination- strings, list_passengers- list
        Input: number,seats, company, destination, list_passengers - the new values
        Output: number,seats, company, destination, list_passengers - accessed through the corresponding initial value defined in the 
        class for each function and modified with the new value
    '''
    def number_setter(self,n):
        if n<0:
            print("Not an available number!")
        else:
            self.__number=n

    def company_setter(self,n):
        if len(n)<1:
            print("Not an available company!")
        else:
            self.__company=n

    def seats_setter(self,n):
        if n<0:
            print("Not an available number of seats!")
        else:
            self.__seats=n

    def destination_setter(self,n):
        if len(n)<1:
            print("Not an available destination!")
        else:
            self.__destination=n

    def passengers_setter(self,n):
        list=[]
        p=Passenger("","",-1)
        if n<0 or n>self.seats_getter():
            print("Not an available number of passengers!")
        else:
            for i in range(0,n):
                list.append(p.read_passenger())
        self.__passengers=list

    def read_plane(self):
        '''
        Descr: reads values for the class attributes
        Precondition: number,seats,n- numbers, company, destination- strings, list_passengers- list
        Input: the class itself
        Output: the class attributes modified with the read values
        '''
        number = int(input("Plane number: "))
        company = input("Plane company: ")
        seats = int(input("Plane number of seats: "))
        destination = input("Plane destination: ")
        n = int(input("Plane number of passengers: "))

        self.number_setter(number)
        self.company_setter(company)
        self.seats_setter(seats)
        self.destination_setter(destination)
        self.passengers_setter(n)

    def string_repr_of_passengers_list(self):
        '''
        Descr: string representation of the passengers list
        Input: the class itself
        Output: the required string representation of the passengers list
        '''
        s=[]
        for elem in self.__passengers:
            s.append(str(elem))
        return s

    def __str__(self):
        '''
        Descr: string representation of the repository
        Input: the class itself
        Output: the required string representation of the repository
        '''
        return ("Number " + str(self.__number)+",company "+self.__company+",number of seats "+str(self.__seats)
                + ",destination "+self.__destination+" Passengers: "
                +str(self.string_repr_of_passengers_list()))

    # 4 . Sort the passengers in a plane by last name
    def sort_passengers_by_lastName(self):
        '''
        Descr: Sorts the passengers in a plane by last name
        Input: the class itself
        Output: the plane object modified
        '''
        self.__passengers.sort(key=lambda x: x.last_getter())

    # 7
    def get_number_passengers_plus_destination(self):
        '''
        Descr: forms a string containing the nr of passengers and the destination of a plane
        Input: the class itself
        Output: the string s
        '''
        s=""
        s+=str(len(self.passengers_getter()))+str(self.destination_getter())
        return s

    # 8
    def passengers_condition8(self):
        '''
        Descr: checks if a plane has passengers with passport numbers starting with the  same 3 letters
        Input: the class itself
        Output: True or False
        '''
        for i in range(0,len(self.__passengers)-1):
            for j in range(i+1,len(self.__passengers)):
                if str(self.__passengers[i].number_getter())[:3]==str(self.__passengers[j].number_getter())[:3]:
                    return True
        return False

    # 9. Identify passengers for which the first name or last name contains a string given as parameter
    def passengers_condition9(self,string):
        '''
        Descr: Identifies passengers for which the first name or last name contains a string given as parameter (from the plane object)
        Input: the class itself, a string
        Output: True or False
        '''
        lst=list(filter(lambda x: x.first_or_last_contains_string(string),self.__passengers))
        s=""
        for elem in lst:
            s+=str(elem)+"\n"
        return s

    # 10
    def if_there_passenger_given_name(self,first,last):
        '''
        Descr: checks if in a plane exists a passenger with a given name
        Input: the class itself, last, first - strings
        Output: True or False
        '''
        for elem in self.__passengers:
            if elem.first_getter()==first and elem.last_getter()==last:
                return True
        return False

    # 11
    def groups_plane_domain(self,k):
        '''
        Descr: Forms groups of k passengers from the plane, but with different last names (k given by the user)
        Input: (self), k -number
        Output: lists of length k
        '''
        if k<=0 or k>len(self.__passengers):
            return ("k is not available")
        else:
            lst=self.__passengers.copy()
            lst.insert(0, self.__passengers[0])

            domain = [i for i in range(0, len(lst))]

            def initSolution():
                return domain[0]

            def getNext(i):
                return i + 1

            def getLast():
                return domain[-1]

            def isSolution(sol, k):
                return len(sol) == k

            def isConsistent(sol, lst):
                for i in range(0, len(sol) - 1):
                    if lst[sol[i]].last_getter() >= lst[sol[-1]].last_getter():
                        return False
                return True

            def groupPersons(groupSize, lst):
                k = 0
                sol = []
                sol.append(initSolution())
                while k >= 0:
                    isSelected = False
                    while (not isSelected) and (sol[k] < getLast()):
                        sol[k] = getNext(sol[k])
                        isSelected = isConsistent(sol, lst)
                    if isSelected:
                        if isSolution(sol, groupSize):
                            yield [lst[i] for i in sol]
                        else:
                            k += 1
                            sol.append(initSolution())
                    else:
                        k -= 1
                        sol.pop()
            s=""
            for group in groupPersons(k, lst):
                s+=str(([str(person) for person in group]))+"\n"
            return s

