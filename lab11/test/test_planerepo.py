from domain.passenger import Passenger
from domain.plane import Plane
from infrastucture.planerepo import PlaneRepo

planerepo = PlaneRepo()

passenger1 = Passenger("l", "s", 123822)
passenger2 = Passenger("lw", "sq", 822222)
passenger3 = Passenger("lf", "so", 123828)
passenger4 = Passenger("lso", "ssis", 123299)

plane1 = Plane(1, "a", 50, "b", [passenger1, passenger2])
plane2 = Plane(2, "c", 90, "d", [passenger1, passenger2, passenger3])
plane3 = Plane(3, "q", 59, "sjsj", [passenger1, passenger2, passenger4, passenger3])

# 1. Get all planes is tested at every string representation

# 2. Add a plane
planerepo.add_plane(plane1)
assert str(planerepo) == ("Number 1,company a,number of seats 50,destination b Passengers: ['Passenger : l s 123822', "
                          "'Passenger : lw sq 822222']\n")

planerepo.add_plane(plane2)
assert str(planerepo) == ("Number 1,company a,number of seats 50,destination b Passengers: ['Passenger : l s 123822', "
                          "'Passenger : lw sq 822222']\nNumber 2,company c,number of seats 90,destination d "
                          "Passengers: ['Passenger : l s 123822', 'Passenger : lw sq 822222', 'Passenger : lf so "
                          "123828']\n")

plane4 = Plane(-3, "q", 59, "sjsj", [passenger1, passenger2, passenger4, passenger3])
planerepo.add_plane(plane4)
assert str(planerepo) == ("Number 1,company a,number of seats 50,destination b Passengers: ['Passenger : l s 123822', "
                          "'Passenger : lw sq 822222']\nNumber 2,company c,number of seats 90,destination d "
                          "Passengers: ['Passenger : l s 123822', 'Passenger : lw sq 822222', 'Passenger : lf so "
                          "123828']\n")

# 3. Delete a plane
planerepo.delete_plane(0)
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : l s 123822', "
                          "'Passenger : lw sq 822222', 'Passenger : lf so 123828']\n")

planerepo.delete_plane(-1)
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : l s 123822', "
                          "'Passenger : lw sq 822222', 'Passenger : lf so 123828']\n")

planerepo.add_plane(plane1)
planerepo.add_plane(plane2)
planerepo.delete_plane(1)
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : l s 123822', "
                          "'Passenger : lw sq 822222', 'Passenger : lf so 123828']\nNumber 2,company c,"
                          "number of seats 90,destination d Passengers: ['Passenger : l s 123822', 'Passenger : lw sq "
                          "822222', 'Passenger : lf so 123828']\n")

planerepo = PlaneRepo()
passenger1 = Passenger("ss", "s", 1120822)
passenger2 = Passenger("ow", "sq", 822222)
passenger3 = Passenger("lf", "so", 123828)
passenger4 = Passenger("lso", "ssis", 123299)

plane1 = Plane(1, "a", 50, "b", [passenger1, passenger2, passenger4, passenger3])
plane2 = Plane(2, "c", 90, "d", [passenger1, passenger2, passenger3])
plane3 = Plane(3, "q", 59, "sjsj", [passenger1, passenger2, passenger4, passenger3])
plane4 = Plane(2, "c", 90, "b", [passenger1, passenger2, passenger3])

planerepo.add_plane(plane1)
planerepo.add_plane(plane2)
planerepo.add_plane(plane3)
planerepo.add_plane(plane4)
# 4. Sort the passengers in a plane by last name given an index


planerepo.sort_passengers_by_lastName_repo(0)
assert str(planerepo) == (
            "Number 1,company a,number of seats 50,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\n"
            + "Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\n"
            + "Number 3,company q,number of seats 59,destination sjsj Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq "
              "822222', 'Passenger : lso ssis 123299', 'Passenger : lf so 123828']\n"
            + "Number 2,company c,number of seats 90,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq "
              "822222', 'Passenger : lf so 123828']\n")

planerepo.sort_passengers_by_lastName_repo(7)
assert str(planerepo) == (
            "Number 1,company a,number of seats 50,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\n"
            + "Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\n"
            + "Number 3,company q,number of seats 59,destination sjsj Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq "
              "822222', 'Passenger : lso ssis 123299', 'Passenger : lf so 123828']\n"
            + "Number 2,company c,number of seats 90,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq "
              "822222', 'Passenger : lf so 123828']\n")

planerepo.sort_passengers_by_lastName_repo(2)
assert str(planerepo) == (
            "Number 1,company a,number of seats 50,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\n"
            + "Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\n"
            + "Number 3,company q,number of seats 59,destination sjsj Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\n"
            + "Number 2,company c,number of seats 90,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq "
              "822222', 'Passenger : lf so 123828']\n")


# 5. Sort planes according to the number of passengers
planerepo.sort_by_number_passengers()
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s "
                          "1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 2,company c,"
                          "number of seats 90,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : ow "
                          "sq 822222', 'Passenger : lf so 123828']\nNumber 1,company a,number of seats 50,destination "
                          "b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq "
                          "822222', 'Passenger : lso ssis 123299']\nNumber 3,company q,number of seats 59,destination "
                          "sjsj Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow "
                          "sq 822222', 'Passenger : lso ssis 123299']\n")

planerepo.delete_plane(0)
planerepo.sort_by_number_passengers()
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination b Passengers: ['Passenger : ss s "
                          "1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 1,company a,"
                          "number of seats 50,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf "
                          "so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\nNumber 3,"
                          "company q,number of seats 59,destination sjsj Passengers: ['Passenger : ss s 1120822', "
                          "'Passenger : lf so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\n")


planerepo.delete_plane(2)
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination b Passengers: ['Passenger : ss s "
                          "1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 1,company a,"
                          "number of seats 50,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf "
                          "so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\n")


planerepo = PlaneRepo()
planerepo.add_plane(plane1)
planerepo.add_plane(plane2)
planerepo.add_plane(plane3)
planerepo.add_plane(plane4)
# 6. Sort planes according to the number of passengers with the first name starting with a given substring
planerepo.sort_condition6("l")
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s "
                          "1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 2,company c,"
                          "number of seats 90,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : ow "
                          "sq 822222', 'Passenger : lf so 123828']\nNumber 1,company a,number of seats 50,destination "
                          "b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq "
                          "822222', 'Passenger : lso ssis 123299']\nNumber 3,company q,number of seats 59,destination "
                          "sjsj Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow "
                          "sq 822222', 'Passenger : lso ssis 123299']\n")
planerepo.sort_condition6("s")
assert str(planerepo)==("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s 1120822', "
                        "'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 2,company c,number of seats "
                        "90,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq 822222', "
                        "'Passenger : lf so 123828']\nNumber 1,company a,number of seats 50,destination b Passengers: "
                        "['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq 822222', "
                        "'Passenger : lso ssis 123299']\nNumber 3,company q,number of seats 59,destination sjsj "
                        "Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq "
                        "822222', 'Passenger : lso ssis 123299']\n")

planerepo.sort_condition6("o")
assert str(planerepo)==("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s 1120822', "
                        "'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 2,company c,number of seats "
                        "90,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq 822222', "
                        "'Passenger : lf so 123828']\nNumber 1,company a,number of seats 50,destination b Passengers: "
                        "['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq 822222', "
                        "'Passenger : lso ssis 123299']\nNumber 3,company q,number of seats 59,destination sjsj "
                        "Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq "
                        "822222', 'Passenger : lso ssis 123299']\n")

# 7. Sort planes according to the string obtained by concatenation of the number of
# passengers in the plane and the destination
planerepo.sort_by_number_passengers_plus_destination()
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination b Passengers: ['Passenger : ss s "
                          "1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 2,company c,"
                          "number of seats 90,destination d Passengers: ['Passenger : ss s 1120822', 'Passenger : ow "
                          "sq 822222', 'Passenger : lf so 123828']\nNumber 1,company a,number of seats 50,destination "
                          "b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq "
                          "822222', 'Passenger : lso ssis 123299']\nNumber 3,company q,number of seats 59,destination "
                          "sjsj Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow "
                          "sq 822222', 'Passenger : lso ssis 123299']\n")
planerepo.delete_plane(0)
planerepo.sort_by_number_passengers_plus_destination()
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s "
                          "1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 1,company a,"
                          "number of seats 50,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf "
                          "so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\nNumber 3,"
                          "company q,number of seats 59,destination sjsj Passengers: ['Passenger : ss s 1120822', "
                          "'Passenger : lf so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\n")

planerepo.delete_plane(2)
planerepo.sort_by_number_passengers_plus_destination()
assert str(planerepo) == ("Number 2,company c,number of seats 90,destination d Passengers: ['Passenger : ss s "
                          "1120822', 'Passenger : ow sq 822222', 'Passenger : lf so 123828']\nNumber 1,company a,"
                          "number of seats 50,destination b Passengers: ['Passenger : ss s 1120822', 'Passenger : lf "
                          "so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis 123299']\n")

planerepo = PlaneRepo()
planerepo.add_plane(plane1)
planerepo.add_plane(plane2)
planerepo.add_plane(plane3)
planerepo.add_plane(plane4)
# 8. Identify planes that have passengers with passport numbers starting with the same 3 letters

assert planerepo.get_planes_passengers_passport_3letters() == ("Number 1,company a,number of seats 50,destination b "
                                                               "Passengers: ['Passenger : ss s 1120822', 'Passenger : "
                                                               "lf so 123828', 'Passenger : ow sq 822222', "
                                                               "'Passenger : lso ssis 123299']\nNumber 3,company q,"
                                                               "number of seats 59,destination sjsj Passengers: ["
                                                               "'Passenger : ss s 1120822', 'Passenger : lf so "
                                                               "123828', 'Passenger : ow sq 822222', 'Passenger : lso "
                                                               "ssis 123299']\n")

planerepo.delete_plane(0)
assert planerepo.get_planes_passengers_passport_3letters() == ("Number 3,company q,number of seats 59,destination "
                                                               "sjsj Passengers: ['Passenger : ss s 1120822', "
                                                               "'Passenger : lf so 123828', 'Passenger : ow sq "
                                                               "822222', 'Passenger : lso ssis 123299']\n")

planerepo.delete_plane(2)
assert planerepo.get_planes_passengers_passport_3letters() == ("Number 3,company q,number of seats 59,destination "
                                                               "sjsj Passengers: ['Passenger : ss s 1120822', "
                                                               "'Passenger : lf so 123828', 'Passenger : ow sq "
                                                               "822222', 'Passenger : lso ssis 123299']\n")


planerepo = PlaneRepo()
planerepo.add_plane(plane1)
planerepo.add_plane(plane2)
planerepo.add_plane(plane3)
planerepo.add_plane(plane4)
# 9. Identify passengers from a given plane for which the first name or last name contains a string given as parameter
plane = plane1
string = "l"
assert planerepo.passengers_condition_9(plane, string) == "Passenger : lf so 123828\nPassenger : lso ssis 123299\n"

plane = plane2
string = "o"
assert planerepo.passengers_condition_9(plane, string) == "Passenger : ow sq 822222\nPassenger : lf so 123828\n"

plane = plane3
string = "k"
assert planerepo.passengers_condition_9(plane, string) == ""


# 10. Identify plane/planes where there is a passenger with given name
first = "lf"
last = "so"
assert planerepo.planes_passenger_name(first, last)==("Number 1,company a,number of seats 50,destination b "
                                                      "Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so "
                                                      "123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis "
                                                      "123299']\nNumber 2,company c,number of seats 90,destination d "
                                                      "Passengers: ['Passenger : ss s 1120822', 'Passenger : ow sq "
                                                      "822222', 'Passenger : lf so 123828']\nNumber 3,company q,"
                                                      "number of seats 59,destination sjsj Passengers: ['Passenger : "
                                                      "ss s 1120822', 'Passenger : lf so 123828', 'Passenger : ow sq "
                                                      "822222', 'Passenger : lso ssis 123299']\nNumber 2,company c,"
                                                      "number of seats 90,destination b Passengers: ['Passenger : ss "
                                                      "s 1120822', 'Passenger : ow sq 822222', 'Passenger : lf so "
                                                      "123828']\n")
first = "lsjsj"
last = "so"
assert planerepo.planes_passenger_name(first, last) == ""

first = "lso"
last = "ssis"
assert planerepo.planes_passenger_name(first, last)==("Number 1,company a,number of seats 50,destination b "
                                                      "Passengers: ['Passenger : ss s 1120822', 'Passenger : lf so "
                                                      "123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis "
                                                      "123299']\nNumber 3,company q,number of seats 59,destination "
                                                      "sjsj Passengers: ['Passenger : ss s 1120822', 'Passenger : lf "
                                                      "so 123828', 'Passenger : ow sq 822222', 'Passenger : lso ssis "
                                                      "123299']\n")

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

# 11
assert planerepo.groups_plane_repo(2,2) == ("['Passenger : Bob John 822222', 'Passenger : Ana Maria 1120822']\n["+"'Passenger : Mihai Ionescu 123299', 'Passenger : Ana Maria 1120822']\n["+"'Passenger : Mihai Ionescu 123299', 'Passenger : Bob John 822222']\n["+"'Passenger : Mihai Ionescu 123299', 'Passenger : Mary James 123828']\n["+"'Passenger : Mary James 123828', 'Passenger : Ana Maria 1120822']\n["
                                            + "'Passenger : Mary James 123828', 'Passenger : Bob John 822222']\n")
assert planerepo.groups_plane_repo(-1,2) == ("Not an available index!")
assert planerepo.groups_plane_repo(2,-1) == ("k is not available")

# 12
assert planerepo.groups_planes_same_destination(4) == ""
assert planerepo.groups_planes_same_destination(9) == "k is not available"
assert planerepo.groups_planes_same_destination(3)== "[\"Number 4,company c,number of seats 90,destination Cluj-Napoca Passengers: ['Passenger : Ana Maria 1120822', 'Passenger : Bob John 822222', 'Passenger : Mary James 123828']\", \"Number 6,company d,number of seats 90,destination Cluj-Napoca Passengers: ['Passenger : Ana Maria 1120822', 'Passenger : Bob John 822222', 'Passenger : Mary James 123828']\", \"Number 3,company q,number of seats 59,destination Cluj-Napoca Passengers: ['Passenger : Ana Maria 1120822', 'Passenger : Bob John 822222', 'Passenger : Mihai Ionescu 123299', 'Passenger : Mary James 123828']\"]\n[\"Number 5,company c,number of seats 90,destination Cluj-Napoca Passengers: ['Passenger : Ana Maria 1120822', 'Passenger : Bob John 822222', 'Passenger : Mary James 123828']\", \"Number 6,company d,number of seats 90,destination Cluj-Napoca Passengers: ['Passenger : Ana Maria 1120822', 'Passenger : Bob John 822222', 'Passenger : Mary James 123828']\", \"Number 3,company q,number of seats 59,destination Cluj-Napoca Passengers: ['Passenger : Ana Maria 1120822', 'Passenger : Bob John 822222', 'Passenger : Mihai Ionescu 123299', 'Passenger : Mary James 123828']\"]\n"
