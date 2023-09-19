from linked_list import LinkedList
import pytest


def test_get_element():

  linked_list = LinkedList()

  linked_list.push_front('a')
  linked_list.push_front('b')
  linked_list.push_front('c')

  assert linked_list.get_element(0) == 'c'
  assert linked_list.get_element(1) == 'b'
  assert linked_list.get_element(2) == 'a'


def test_count_element():

  linked_list = LinkedList()

  assert linked_list.count() == 0

  linked_list.push_front('a')
  linked_list.push_front('b')
  linked_list.push_front('c')

  assert linked_list.count() == 3


def test_pop_front():

  linked_list = LinkedList()

  linked_list.push_front('a')
  linked_list.push_front('b')
  linked_list.push_front('c')

  assert linked_list.pop_front() == 'c'


def test_insert_after():

  linked_list = LinkedList()

  linked_list.push_front('a')
  linked_list.push_front('b')
  linked_list.push_front('c')
  linked_list.insert_after(1, "e")

  assert linked_list.get_element(2) == "e"
  assert linked_list.get_element(1) == "b"

def test_remove_element():

  linked_list = LinkedList()

  linked_list.push_front('a')
  linked_list.push_front('b')
  linked_list.push_front('c')
  linked_list.remove_element(1)

  assert linked_list.get_element(1) == "a"
  assert linked_list.get_element(0) == "c"

def test_reverse():

  linked_list = LinkedList()

  linked_list.push_front('a')
  linked_list.push_front('b')
  linked_list.push_front('c')
  linked_list.reverse()
  

  assert linked_list.get_element(1) == "b"
  assert linked_list.get_element(0) == "a"
# have pytest run all test cases present in this file)

pytest.main([__file__])
