from domain.passenger import Passenger
from domain.plane import Plane


def test_plane_class():
    passengers = [
        Passenger("John", "Doe", 123),
        Passenger("Jane", "Smith", 456),
        Passenger("Alice", "Johnson", 789)
    ]
    plane = Plane(1, "Airline", 50, "Destination", passengers)

    assert plane.number_getter() == 1
    assert plane.company_getter() == "Airline"
    assert plane.seats_getter() == 50
    assert plane.destination_getter() == "Destination"
    assert plane.passengers_getter() == passengers

    # Test setters
    plane.number_setter(2)
    plane.company_setter("New Airline")
    plane.seats_setter(60)
    plane.destination_setter("New Destination")

    assert plane.number_getter() == 2
    assert plane.company_getter() == "New Airline"
    assert plane.seats_getter() == 60
    assert plane.destination_getter() == "New Destination"

    # Test passengers_setter method
    new_passengers = [
        Passenger("Bob", "Johnson", 111),
        Passenger("Eva", "Smith", 222),
        Passenger("Charlie", "Brown", 333)
    ]
    plane.passengers_setter(3)
    # the user should read exactly the values given above
    assert plane.string_repr_of_passengers_list() == ['Passenger : Bob Johnson 111', 'Passenger : Eva Smith 222', 'Passenger : Charlie Brown 333']

    # Test string_repr_of_passengers_list method
    assert plane.string_repr_of_passengers_list() == [
        "Passenger : Bob Johnson 111",
        "Passenger : Eva Smith 222",
        "Passenger : Charlie Brown 333"
    ]

    # Test __str__ method
    assert str(plane) == ("Number 2,company New Airline,number of seats 60,destination New Destination Passengers: ["
                          "'Passenger : Bob Johnson 111', 'Passenger : Eva Smith 222', 'Passenger : Charlie Brown "
                          "333']")

    # Test sort_passengers_by_lastName method
    plane.sort_passengers_by_lastName()
    assert plane.string_repr_of_passengers_list() == [
        "Passenger : Charlie Brown 333",
        "Passenger : Bob Johnson 111",
        "Passenger : Eva Smith 222"
    ]

    # Test get_number_passengers_plus_destination method
    assert plane.get_number_passengers_plus_destination() == "3New Destination"

    # Test passengers_condition8 method
    assert not plane.passengers_condition8()

    # Test passengers_condition9 method
    assert plane.passengers_condition9("ohn") == "Passenger : Bob Johnson 111\n"

    # Test if_there_passenger_given_name method
    assert plane.if_there_passenger_given_name("Bob", "Johnson")
    assert not plane.if_there_passenger_given_name("John", "Doe")




# Run the test
test_plane_class()
