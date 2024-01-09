from domain.passenger import Passenger


def test_passenger_class():
    # Test the constructor
    passenger1 = Passenger("j", "d", 123)
    assert passenger1.first_getter() == "j"
    assert passenger1.last_getter() == "d"
    assert passenger1.number_getter() == 123
    assert str(passenger1) == "Passenger : j d 123"

    # Test setters, getters and string representation
    passenger1.first_setter("j")
    passenger1.last_setter("s")
    passenger1.number_setter(456)

    assert passenger1.first_getter() == "j"
    assert passenger1.last_getter() == "s"
    assert passenger1.number_getter() == 456
    assert str(passenger1) == "Passenger : j s 456"

    passenger1.first_setter("k")
    passenger1.last_setter("l")
    passenger1.number_setter(4568)

    assert passenger1.first_getter() == "k"
    assert passenger1.last_getter() == "l"
    assert passenger1.number_getter() == 4568

    passenger1.first_setter("jsa")
    passenger1.last_setter("s")
    passenger1.number_setter(456)
    assert str(passenger1) == "Passenger : jsa s 456"

    assert passenger1.first_getter() == "jsa"
    assert passenger1.last_getter() == "s"
    assert passenger1.number_getter() == 456
    assert str(passenger1) == "Passenger : jsa s 456"

    passenger2 = Passenger("Alice", "Johnson", 789)
    assert passenger2.first_getter() == "Alice"
    assert passenger2.last_getter() == "Johnson"
    assert passenger2.number_getter() == 789

    # Test first_starts_with_string
    passenger3 = Passenger("Peter", "Parker", 111)
    assert passenger3.first_starts_with_string("Pet")
    assert not passenger3.first_starts_with_string("Peterr")

    passenger3 = Passenger("eter", "Parker", 111)
    assert passenger3.first_starts_with_string("et")
    assert not passenger3.first_starts_with_string("Peterr")

    passenger3 = Passenger("er", "Parker", 111)
    assert passenger3.first_starts_with_string("er")
    assert not passenger3.first_starts_with_string("Peterr")

    # Test first_or_last_contains_string
    passenger4 = Passenger("Mary", "ary", 222)
    assert passenger4.first_or_last_contains_string("ary")
    assert not passenger4.first_or_last_contains_string("Peter")

    passenger4 = Passenger("Mary", "Jane", 222)
    assert passenger4.first_or_last_contains_string("ary")
    assert not passenger4.first_or_last_contains_string("Peter")

    passenger4 = Passenger("Mary", "", 222)
    assert passenger4.first_or_last_contains_string("ary")
    assert not passenger4.first_or_last_contains_string("Peter")


test_passenger_class()