

class Passenger:
    '''
    Descr: contains the initial, string representation, setters, getters
    and different functions and features for a passenger
    '''

    def __init__(self,first,last,number):
        '''
        Descr: initializes the attributes of a passenger in the class
        Precondition: first, last - string , number-number
        Input: (self),first, last, number
        '''

        if first!="":
            self.__first=first
        else:
            self.__first=""

        if last!="":
            self.__last=last
        else:
            self.__last=""

        if number>=0:
            self.__number=number
        else:
            self.__number=-1
    '''
    Descr: each getter function returns an attribute of a passenger predefined in the class
    Input: the class itself
    Output: first, last, number- accessed through the corresponding initial value defined in the class for each function
    '''
    def first_getter(self):
        return self.__first

    def last_getter(self):
        return self.__last

    def number_getter(self):
        return self.__number

    '''
        Descr: each setter function changes a specific attribute of a passenger, predefined variables in the class, with new 
        values
        Precondition: first, last - string , number-number
        Input: first, last - string , number-number- the new values
        Output: first, last - string , number-number - accessed through the corresponding initial value defined in the 
        class for each function and modified with the new value
    '''
    def first_setter(self,f):
        if f!="":
            self.__first=f
        else:
            print("Not an available first name!")

    def last_setter(self,f):
        if f!="":
            self.__last=f
        else:
            print("Not an available last name!")

    def number_setter(self,f):
        if f!="":
            self.__number=f
        else:
            print("Not an available number!")

    def __str__(self):
        '''
        Descr: string representation of a passenger
        Input: the class itself
        Output: the string representation of the object
        '''
        return "Passenger : "+self.__first+" "+self.__last+" "+str(self.__number)

    def read_passenger(self):
        '''
        Descr: reads values for the class attributes
        Precondition: first, last - string , number-number
        Input: the class itself
        Output: the class attributes modified with the read values
        '''
        f=input("First name: ")
        l = input("Last name: ")
        n= int(input("Number: "))
        return Passenger(f, l, n)

    # 6 . First name starts with a given substring
    def first_starts_with_string(self, string):
        '''
        Descr: checks if the first name of the passenger object starts with a given string
        Input: the class itself, a given string
        Output: True or False
        '''
        return self.first_getter()[:len(string)]==string

    # 8 . First name or last name contains a string given as parameter
    def first_or_last_contains_string(self,string):
        '''
        Descr: checks if the first name or last name contains a string given as parameter
        Input: the class itself, a given string
        Output: True or False
        '''
        return (string in self.first_getter()) or (string in self.last_getter())



