from domain.passenger import Passenger
from domain.plane import Plane
from infrastucture.planerepo import PlaneRepo

planerepo=PlaneRepo()
passenger1=Passenger("Ana","Maria",1120822)
passenger2=Passenger("Bob","John",822222)
passenger3=Passenger("Mary","James",123828)
passenger4=Passenger("Mihai","Ionescu",123299)
passenger5=Passenger("Dragos","John",822322)

plane1=Plane(1,"a",50,"Bucharest",[passenger1,passenger2,passenger4,passenger3])
plane2=Plane(2,"c",90,"Bucharest",[passenger1,passenger2,passenger5,passenger3])
plane3=Plane(3,"q",59,"Cluj-Napoca",[passenger1,passenger2,passenger4,passenger3])
plane4=Plane(4,"c",90,"Cluj-Napoca",[passenger1,passenger2,passenger3])
plane5=Plane(5,"c",90,"Cluj-Napoca",[passenger1,passenger2,passenger3])
plane6=Plane(6,"d",90,"Cluj-Napoca",[passenger1,passenger2,passenger3])

planerepo.add_plane(plane1)
planerepo.add_plane(plane2)
planerepo.add_plane(plane3)
planerepo.add_plane(plane4)
planerepo.add_plane(plane5)
planerepo.add_plane(plane6)

'''
#2nd example
planerepo=PlaneRepo()
passenger1=Passenger("ss","s",1120822)
passenger3=Passenger("lf","so",123828)
passenger4=Passenger("lso","ssis",123299)

plane1=Plane(1,"a",50,"b",[passenger1,passenger4,passenger3])
plane2=Plane(2,"c",90,"d",[passenger1,passenger3])
plane3=Plane(3,"q",59,"sjsj",[passenger1,passenger4,passenger3])
plane4=Plane(2,"c",90,"b",[passenger1,passenger3])

planerepo.add_plane(plane1)
planerepo.add_plane(plane3)
planerepo.add_plane(plane4)
'''

'''
# 3rd example
planerepo=PlaneRepo()
passenger1=Passenger("ss","s",1120822)
passenger2=Passenger("ow","sq",822222)
passenger3=Passenger("lf","so",123828)
passenger4=Passenger("lso","ssis",123299)

plane1=Plane(1,"a",50,"b",[passenger1,passenger2,passenger4,passenger3])
plane2=Plane(2,"c",90,"d",[passenger1,passenger2,passenger3])
plane3=Plane(3,"q",59,"sjsj",[passenger1,passenger2,passenger4,passenger3])
plane4=Plane(2,"c",90,"b",[passenger1,passenger2,passenger3])
plane5=Plane(2,"sj",90,"q",[passenger2,passenger3])

planerepo.add_plane(plane1)
planerepo.add_plane(plane2)
planerepo.add_plane(plane3)
planerepo.add_plane(plane4)
planerepo.add_plane(plane5)
'''


def read_option():
    option=int(input("Read option: "))
    return option

def print_menu():
    s=""
    s+=("MENU:\n\t1. Get all panes\n\t2. Add a plane\n\t3. Delete a plane\n"
        + "\t4. Sort the passengers in a plane by last name given an index\n"
        + "\t5. Sort planes according to the number of passengers\n"
        + "\t6. Sort planes according to the number of passengers"
        + " with the first name starting with a given substring\n"
        + "\t7. Sort planes according to the string obtained by concatenation of the number "
        + "of  passengers in the plane and the destination\n"
        + "\t8. Identify planes that have passengers with passport "
        + "numbers starting with the same 3 letters\n"
        + "\t9. Identify passengers from a given plane for which the first name "
        + "or last name contains a string given as parameter\n"
        + "\t10. Identify plane/planes where there is a passenger with given name\n"
        + "\t11. Form groups of k passengers from the same plane, but with different last names (k given by the user)\n"
        +"\t12 . Form groups of k planes with the same destination but belonging to different airplane companies (k given by the user)\n"
          "\t0. STOP\n")
    return s


def start():
    stop=False
    while stop==False:
        print(print_menu())
        option=read_option()
        if option==1:
            print(str(planerepo))
        elif option==2:
            p=planerepo.read_plane_repo()
            planerepo.add_plane(p)
            print(str(planerepo))
        elif option == 3:
            index=int(input("Read an index: "))
            planerepo.delete_plane(index)
            print(str(planerepo))
        elif option == 4 :
            index = int(input("Read an index: "))
            planerepo.sort_passengers_by_lastName_repo(index)
            print(str(planerepo))
        elif option == 5:
            planerepo.sort_by_number_passengers()
            print(str(planerepo))
        elif option == 6:
            string = input("Read a string: ")
            planerepo.sort_condition6(string)
            print(str(planerepo))
        elif option == 7:
            planerepo.sort_by_number_passengers_plus_destination()
            print(str(planerepo))
        elif option == 8:
            print(planerepo.get_planes_passengers_passport_3letters())
        elif option == 9:
            plane=planerepo.read_plane_repo()
            string=input("Read a string: ")
            print(planerepo.passengers_condition_9(plane,string))
        elif option == 10:
            first = input("Read first name: ")
            last = input("Read last name: ")
            print(planerepo.planes_passenger_name(first, last))
        elif option == 11:
            index = int(input("Read an index for the plane: "))
            k = int(input("Read k: "))
            print(planerepo.groups_plane_repo(index,k))
        elif option == 12:
            k = int(input("Read k: "))
            print(planerepo.groups_planes_same_destination(k))
        elif option==0:
            stop=True
        else:
            print("Not an available option!")




