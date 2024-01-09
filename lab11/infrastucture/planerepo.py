from domain.plane import Plane


class PlaneRepo:
    # Descr: contains the container with all the planes
    def __init__(self):
        self.__data=[]

    '''
    Descr: the getter function and setter function return, respectively change the repository container at 
    a specific moment
    Input: the class itself
    Output: the container itself(in getter), respectively the container changed(in setter)
    '''

    def planes_getter(self):
        return self.__data

    def planes_setter(self,planes):
        self.__data=planes

    def __str__(self):
        # the string representation of the container
        s=""
        for i in range(0,len(self.__data)):
            if len(str(self.__data[i]))!=0:
                s+=str(self.__data[i])+"\n"
        return s

    # 1 . Add a plane
    def add_plane(self,plane):
        '''
        Descr: adds a plane to the repository (if the conditions similar to the ones in the constructor
        of Plane class are fulfilled)
        Precondition: plane is of type Plane
        Input: (self),plane of type Plane
        Output: our self.__data(modified)
        '''
        if (plane.number_getter()>=0 and len(plane.company_getter())>=1 and plane.seats_getter()>=1
                and plane.destination_getter()!="" and len(plane.passengers_getter())<=plane.seats_getter()):
            self.__data.append(plane)
        else:
            print("Not an available plane!")

    # 2 . Delete a plane
    def delete_plane(self,index):
        '''
        Descr: deletes a plane at given index
        Precondition: index-number
        Input: (self),index
        Output: our self.__data(modified)
        '''
        if index<0 or index>=len(self.__data):
            print("Not an available index!")
        else:
            del self.__data[index]

    def read_plane_repo(self):
        # Descr: imports the read_plane() function, so as to maintain a layered arhitecture
        plane = Plane(-1, "", -1, "", [])
        plane.read_plane()
        return plane

    # 4 . Sort the passengers in a plane by last name given an index
    def sort_passengers_by_lastName_repo(self,index):
        '''
        Descr: Sorts the passengers in a plane at a given index by last name
        Precondition: index-number
        Input: (self),index
        Output: our self.__data(modified)
        '''
        if index<0 or index>=len(self.__data):
            print("Not an available index!")
        else:
            self.__data[index].sort_passengers_by_lastName()

    # 5. Sort planes according to the number of passengers
    def sort_by_number_passengers(self):
        '''
        Descr: Sorts planes according to the number of passengers
        Input: (self)
        Output: our self.__data(modified)
        '''
        self.__data.sort(key=lambda x: len(x.passengers_getter()))

    # 6 . Sort planes according to the number of passengers with the first name starting with a given substring
    def sort_condition6(self,string):
        '''
        Descr: Sorts planes according to the number of passengers with the first name starting with a given substring
        Input: (self), string- a string
        Output: our self.__data(modified)
        '''
        self.__data.sort(key=lambda x: x.passengers_getter_special(string))

    # 7. Sort planes according to the string obtained by concatenation of the number
    # of  passengers in the plane and the destination
    def sort_by_number_passengers_plus_destination(self):
        '''
        Descr: Sorts planes according to the string obtained by concatenation of the number of  passengers in the plane and the destination
        Input: (self)
        Output: our self.__data(modified)
        '''
        self.__data.sort(key=lambda x:x.get_number_passengers_plus_destination())

    # 8. Identify planes that have passengers with passport numbers starting with the same 3 letters
    def get_planes_passengers_passport_3letters(self):
        '''
        Descr: Identifies planes that have passengers with passport numbers starting with the same 3 letters
        Input: (self)
        Output: s - string
        '''
        lst=list(filter(lambda x:x.passengers_condition8(), self.__data))
        s=""
        for elem in lst:
            s+=str(elem)+"\n"
        return s

    # 9. Identify passengers from a given plane for which the first name or last name contains a
    # string given as parameter
    def passengers_condition_9(self,plane,string):
        '''
        Descr: Identify passengers from a given plane for which the first name or last name contains string given as parameter
        Input: (self), plane of type Plane , string - string
        Output: result provided by the function passengers_condition9 for our given plane object
        '''
        return plane.passengers_condition9(string)

    # 10 . Identify plane/planes where there is a passenger with given name
    def planes_passenger_name(self,first,last):
        '''
        Descr: Identifies planes where there is a passenger with given name
        Input: (self), first, last - strings
        Output: s - string
        '''
        lst=list(filter(lambda x:x.if_there_passenger_given_name(first,last),self.__data))
        s=""
        for elem in lst:
            s+=str(elem)+"\n"
        return s

    # 11 . Form groups of k passengers from the same plane, but with different last names (k given by the user)
    def groups_plane_repo(self,index,k):
        '''
        Descr: uses the function groups_plane_domain() from the Plane class
        Input: (self), index, k -numbers
        Output: lists of length k
        '''
        if index<0 or index>=len(self.__data):
            return ("Not an available index!")
        else:
            return self.__data[index].groups_plane_domain(k)

    # 12 . Form groups of k planes with the same destination but belonging to different airplane companies
    # (k given by the user)
    def groups_planes_same_destination(self,k):
        '''
        Descr: Form groups of k planes with the same destination but belonging to different airplane companies
        Input: (self), k -number
        Output: lists of length k
        '''
        if k<=0 or k>len(self.__data):
            return ("k is not available")
        else:

            lst=self.__data
            lst.insert(0, self.__data[0])

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
                    if lst[sol[i]].company_getter() >= lst[sol[-1]].company_getter() or lst[sol[i]].destination_getter()!=lst[sol[-1]].destination_getter():
                        return False
                return True

            def groupPlanes(groupSize, lst):
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
            for repo in groupPlanes(k, lst):
                s+=str([str(plane) for plane in repo])+"\n"
            return s
