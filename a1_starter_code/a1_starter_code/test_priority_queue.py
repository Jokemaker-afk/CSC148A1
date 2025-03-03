"""Assignment 1 - Tests for class PriorityQueue  (Task 3a)

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

All of the files in this directory are
Copyright (c) Jonathan Calver, Diane Horton, Sophia Huynh, Joonho Kim and
Jacqueline Smith.

Module Description:
This module will contain tests for class PriorityQueue.
"""
from container import PriorityQueue
from event import CloseLine


class Test_PriorityQueue:
    def test_init_empty(self) -> None:
        """Test if init is empty"""
        lst = PriorityQueue()
        assert lst.is_empty()

    def test_init_with_1_str(self) -> None:
        """Test init contain 1 str"""
        lst = PriorityQueue()
        lst.add("a")
        assert not lst.is_empty()
        assert lst.remove() == "a"
        assert lst.is_empty()

    def test_init_with_1_int(self) -> None:
        """Test init contain 1 int"""
        lst = PriorityQueue()
        lst.add(1)
        assert not lst.is_empty()
        assert lst.remove() == 1
        assert lst.is_empty()

    def test_init_with_more(self) -> None:
        """Test init contain more str"""
        lst = PriorityQueue()
        lst.add("k")
        lst.add("a")
        lst.add("j")
        assert not lst.is_empty()
        lst.remove()
        lst.remove()
        assert lst.remove() == "k"
        assert lst.is_empty()

    def test_init_with_more_int(self) -> None:
        """Test init contain more int"""
        lst = PriorityQueue()
        lst.add(2)
        lst.add(1)
        lst.add(3)
        assert not lst.is_empty()
        lst.remove()
        lst.remove()
        assert lst.remove() == 3
        assert lst.is_empty()

    def test_remove_1_str(self) -> None:
        """Test remove 1 str"""
        lst = PriorityQueue()
        lst.add("k")
        assert lst.remove() == "k"
        assert lst.is_empty()

    def test_remove_2_str(self) -> None:
        """Test remove 2 str"""
        lst = PriorityQueue()
        lst.add("k")
        lst.add("h")
        assert lst.remove() == "h"
        assert lst.remove() == "k"
        assert lst.is_empty()

    def test_remove_more_str(self) -> None:
        """Test remove more str"""
        lst = PriorityQueue()
        lst.add("k")
        lst.add("hasd")
        lst.add("z")
        assert lst.remove() == "hasd"
        assert lst.remove() == "k"
        assert lst.remove() == "z"
        assert lst.is_empty()

    def test_remove_1_int(self) -> None:
        """Test remove 1 int"""
        lst = PriorityQueue()
        lst.add(1)
        assert lst.remove() == 1
        assert lst.is_empty()

    def test_remove_2_int(self) -> None:
        """Test remove 2 int"""
        lst = PriorityQueue()
        lst.add(1)
        lst.add(2)
        assert lst.remove() == 1
        assert lst.remove() == 2
        assert lst.is_empty()

    def test_remove_more_int(self) -> None:
        """Test remove more int"""
        lst = PriorityQueue()
        lst.add(1)
        lst.add(2)
        lst.add(567)
        assert lst.remove() == 1
        assert lst.remove() == 2
        assert lst.remove() == 567
        assert lst.is_empty()

    def test_remove_1_list_any(self) -> None:
        """Test remove 1 list"""
        lst = PriorityQueue()
        lst.add([1])
        assert lst.remove() == [1]
        assert lst.is_empty()

    def test_remove_2_list_any(self) -> None:
        """Test remove 2 list"""
        lst = PriorityQueue()
        lst.add([2])
        lst.add([1])
        assert lst.remove() == [1]
        assert lst.remove() == [2]
        assert lst.is_empty()

    def test_remove_more_list_any(self) -> None:
        """Test remove more list"""
        lst = PriorityQueue()
        lst.add([3])
        lst.add([2])
        lst.add([1])
        assert lst.remove() == [1]
        assert lst.remove() == [2]
        assert lst.remove() == [3]
        assert lst.is_empty()

    def test_is_empty_0(self) -> None:
        """Test is_empty with 0 item"""
        lst = PriorityQueue()
        assert lst.is_empty()

    def test_is_empty_1(self) -> None:
        """Test is_empty with 1 item"""
        lst = PriorityQueue()
        lst.add(1)
        assert not lst.is_empty()
        lst.remove()
        assert lst.is_empty()
        lst.add([0])
        assert not lst.is_empty()
        lst.remove()
        assert lst.is_empty()
        lst.add("a")
        assert not lst.is_empty()
        lst.remove()
        assert lst.is_empty()

    def test_is_empty_more(self) -> None:
        """Test is_empty with more item"""
        lst = PriorityQueue()
        lst.add(1)
        lst.add(2)
        lst.add(7)
        assert not lst.is_empty()
        lst.remove()
        lst.remove()
        lst.remove()
        assert lst.is_empty()

    def test_add_1_str(self) -> None:
        """Test add with 1 str"""
        lst = PriorityQueue()
        lst.add("a")
        assert lst.remove() == "a"

    def test_add_2_str(self) -> None:
        """Test add with 2 str not in order"""
        lst = PriorityQueue()
        lst.add('fred')
        lst.add('anna')
        assert lst.remove() == 'anna'  # check the first one is 'anna'
        assert lst.remove() == 'fred'  # check the second is 'fred'

    def test_add_more_str(self) -> None:
        """Test add with more str"""
        lst = PriorityQueue()
        lst.add('fred')
        lst.add('mona')
        lst.add('anna')
        assert lst.remove() == 'anna'  # check the first one is 'anna'
        assert lst.remove() == 'fred'  # check the second is 'fred'
        assert lst.remove() == 'mona'  # check the second is 'mona'

    def test_add_more_str_with_eq(self) -> None:
        """Test add with more str with equal"""
        lst = PriorityQueue()
        lst.add('fred')
        lst.add('mona')
        lst.add('fred')
        assert lst.remove() == 'fred'  # check the first one is 'fred'
        assert lst.remove() == 'fred'  # check the second is 'fred'
        assert lst.remove() == 'mona'  # check the second is 'mona'

    def test_add_1_int(self) -> None:
        """Test add with 1 int"""
        lst = PriorityQueue()
        lst.add(1)
        assert lst.remove() == 1

    def test_add_2_int_order(self) -> None:
        """Test add with 2 int in order"""
        lst = PriorityQueue()
        lst.add(1)
        lst.add(7)
        assert lst.remove() == 1
        assert lst.remove() == 7

    def test_add_2_int_not_order(self) -> None:
        """Test add with 2 int in order"""
        lst = PriorityQueue()
        lst.add(7)
        lst.add(1)
        assert lst.remove() == 1
        assert lst.remove() == 7

    def test_add_more_int_order(self) -> None:
        """Test add with more int in order"""
        lst = PriorityQueue()
        lst.add(1)
        lst.add(4)
        lst.add(7)
        assert lst.remove() == 1
        assert lst.remove() == 4
        assert lst.remove() == 7

    def test_add_more_int_not_order(self) -> None:
        """Test add with 3 int not in order"""
        lst = PriorityQueue()
        lst.add(7)
        lst.add(4)
        lst.add(1)
        assert lst.remove() == 1
        assert lst.remove() == 4
        assert lst.remove() == 7

    def test_add_more_int_not_order_with_eq(self) -> None:
        """Test add with 3 int with 2 of them equal"""
        lst = PriorityQueue()
        lst.add(1)
        lst.add(4)
        lst.add(1)
        assert lst.remove() == 1
        assert lst.remove() == 1
        assert lst.remove() == 4

    def test_add_2_event_with_equal(self) -> None:
        """Test add with 2 objects of Event"""
        lst = PriorityQueue()
        lst.add(CloseLine(2, 5))
        lst.add(CloseLine(2, 3))
        assert lst.remove() == CloseLine(2, 5)
        assert lst.remove() == CloseLine(2, 3)

    def test_add_more_event_with_equal(self) -> None:
        """Test add with more object in order"""
        lst = PriorityQueue()
        lst.add(CloseLine(5, 5))
        lst.add(CloseLine(2, 5))
        lst.add(CloseLine(2, 3))
        assert lst.remove() == CloseLine(2, 5)
        assert lst.remove() == CloseLine(2, 3)
        assert lst.remove() == CloseLine(5, 5)


if __name__ == '__main__':
    import pytest

    pytest.main(['test_priority_queue.py'])
