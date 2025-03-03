"""Assignment 1 - Grocery Store Simulation

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Joonho Kim and
Jacqueline Smith.

Module Description:
This module contains some starter tests for Assignment 1.
You may add additional tests here, but you will not hand in this file.
"""
from io import StringIO
from simulation import GroceryStoreSimulation
from event import create_event_list
from store import GroceryStore, Customer, Item
from store import RegularLine, ExpressLine, SelfServeLine

CONFIG_FILE = '''{
  "regular_count": 1,
  "express_count": 0,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''

EVENT_FILE = '''10 Arrive Tamara Bananas 7
5 Arrive Jugo Bread 3 Cheese 3
'''


# a provided sample test for the whole simulation
def test_simulation() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
    gss.run(create_event_list(StringIO(EVENT_FILE)))
    assert gss.stats == {'num_customers': 2, 'total_time': 18, 'max_wait': 8}


# Note: You can write additional tests here or in a separate file
# You will hand in this file. The only tests you will hand in are your tests
# for class PriorityQueue in file test_container.py.


CONFIG_FILE_2 = '''{
  "regular_count": 0,
  "express_count": 1,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''


def test_simulation_express() -> None:
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE_2))
    gss.run(create_event_list(StringIO(EVENT_FILE)))
    assert gss.stats == {'num_customers': 2, 'total_time': 18, 'max_wait': 8}


CONFIG_FILE_3 = '''{
  "regular_count": 0,
  "express_count": 0,
  "self_serve_count": 1,
  "line_capacity": 1
}
'''


def test_simulation_self_serve() -> None:
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE_3))
    gss.run(create_event_list(StringIO(EVENT_FILE)))
    assert gss.stats == {'num_customers': 2, 'total_time': 31, 'max_wait': 21}


CONFIG_FILE_CLOSE = '''{
  "regular_count": 2,
  "express_count": 0,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''

EVENT_FILE_CLOSE = '''10 Arrive Tamara Bananas 7
5 Arrive Jugo Bread 3 Cheese 3
0 Close 0
'''


def test_simulation_close() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE_CLOSE))
    gss.run(create_event_list(StringIO(EVENT_FILE_CLOSE)))
    assert gss.stats == {'num_customers': 2, 'total_time': 18, 'max_wait': 8}


TEST_BASE_111_10 = '''{
    "regular_count": 1,
    "express_count": 1,
    "self_serve_count": 1,
    "line_capacity": 10
}'''


def test_simulation_base_111_10() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(TEST_BASE_111_10))
    event_file_name = "input_files/events_base.txt"
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    gss.run(events)
    assert gss.stats == {'num_customers': 6, 'total_time': 87, 'max_wait': 22}


TEST_BASE_300_01 = '''{
  "regular_count": 3,
  "express_count": 0,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''


def test_simulation_base_300_01() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(TEST_BASE_300_01))
    event_file_name = "input_files/events_base.txt"
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    gss.run(events)
    assert gss.stats == {'num_customers': 6, 'total_time': 76, 'max_wait': 11}


TEST_EVENT_ONE_AT_A_TIME_100_10 = '''{
  "regular_count": 1,
  "express_count": 0,
  "self_serve_count": 0,
  "line_capacity": 10
}
'''


def test_simulation_base_events_one_at_a_time_100_10() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(TEST_EVENT_ONE_AT_A_TIME_100_10))
    event_file_name = "input_files/events_one_at_a_time.txt"
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    gss.run(events)
    assert gss.stats == {'num_customers': 3, 'total_time': 21, 'max_wait': 3}


TEST_EVENT_ONE_AT_A_TIME_001_10 = '''{
  "regular_count": 0,
  "express_count": 0,
  "self_serve_count": 1,
  "line_capacity": 10
}
'''


def test_simulation_events_one_at_a_time_001_10() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(TEST_EVENT_ONE_AT_A_TIME_001_10))
    event_file_name = "input_files/events_one_at_a_time.txt"
    with open(event_file_name) as event_file:
        events = create_event_list(event_file)
    gss.run(events)
    assert gss.stats == {'num_customers': 3, 'total_time': 24, 'max_wait': 6}


if __name__ == '__main__':
    import pytest

    pytest.main(['test_a1.py'])
