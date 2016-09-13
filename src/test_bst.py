#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from bst import Node, Bst
import pytest


def test_node_init_value():
    """
    Test that a new instance of Node(value) has self.value == value.
    """
    node = Node(3)
    assert node.value == 3


def test_node_init_selfleft():
    """
    Test that a new instance of Node(value) has self.left == None.
    """
    node = Node(3)
    assert node.left is None


def test_node_init_selfright():
    """
    Test that a new instance of Node(value) has self.right == None.
    """
    node = Node(3)
    assert node.right is None


def test_compare_self_to_a_bigger_node1():
    """
    Test that function compare_self_to_a_node(self, n)
    assigns n.left = self.value if self.value is smaller than n.value.
    """
    node1 = Node(3)
    node2 = Node(5)
    node1.compare_self_to_a_node(node2)
    assert node2.left.value == 3


def test_compare_self_to_a_bigger_node2():
    """
    Test that function compare_self_to_a_node(self, n)
    doesn't change n.right = None if self.value is smaller than n.value.
    """
    node1 = Node(3)
    node2 = Node(5)
    node1.compare_self_to_a_node(node2)
    assert node2.right is None


def test_compare_self_to_a_smaller_node1():
    """
    Test that function compare_self_to_a_node(self, n)
    assigns n.right = self.value if self.value is bigger than n.value.
    """
    node1 = Node(7)
    node2 = Node(5)
    node1.compare_self_to_a_node(node2)
    assert node2.right.value == 7


def test_compare_self_to_a_smaller_node2():
    """
    Test that function compare_self_to_a_node(self, n)
    doesn't change n.left = None if self.value is bigger than n.value.
    """
    node1 = Node(7)
    node2 = Node(5)
    node1.compare_self_to_a_node(node2)
    assert node2.left is None


def test_compare_self_to_equal_value1():
    """
    Test that function compare_self_to_a_node(self, n)
    doesn't change n.left = None if self.value is equal to n.value.
    """
    node1 = Node(7)
    node2 = Node(7)
    node1.compare_self_to_a_node(node2)
    assert node2.left is None


def test_compare_self_to_equal_value2():
    """
    Test that function compare_self_to_a_node(self, n)
    doesn't change n.right = None if self.value is equal to n.value.
    """
    node1 = Node(7)
    node2 = Node(7)
    node1.compare_self_to_a_node(node2)
    assert node2.right is None


def test_bst_init():
    bst = Bst()
    assert bst.head is None


@pytest.fixture(scope='function')
def bst_empty():
    bst = Bst()
    return bst


def test_insert(bst_empty):
    bst_empty.insert(5)
    assert bst_empty.head.value == 5


def test_insert_left1(bst_empty):
    bst_empty.insert(5)
    bst_empty.insert(1)
    assert bst_empty.head.left.value == 1


def test_insert_right1(bst_empty):
    bst_empty.insert(5)
    bst_empty.insert(10)
    assert bst_empty.head.right.value == 10


@pytest.fixture(scope='function')
def bst_3():
    bst = Bst()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.node_left = bst.head.left
    bst.node_right = bst.head.right
    return bst


def test_insert_left_left(bst_3):
    bst_3.insert(2)
    assert bst_3.node_left.left.value == 2


def test_insert_left_right(bst_3):
    bst_3.insert(7)
    assert bst_3.node_left.right.value == 7


def test_insert_right_left(bst_3):
    bst_3.insert(12)
    assert bst_3.node_right.left.value == 12


def test_insert_right_right(bst_3):
    bst_3.insert(17)
    assert bst_3.node_right.right.value == 17


def test_contains_true5(bst_3):
    assert bst_3.contains(5) is True


def test_contains_true15(bst_3):
    assert bst_3.contains(15) is True


def test_contains_true10(bst_3):
    assert bst_3.contains(10) is True


def test_contains_false(bst_3):
    assert bst_3.contains(6) is False


def test_contains_empty(bst_empty):
    assert bst_empty.contains(5) is False


def test_size_empty(bst_empty):
    assert bst_empty.size() == 0


def test_size_3(bst_3):
    assert bst_3.size() == 3


def test_size_4(bst_3):
    bst_3.insert(18)
    assert bst_3.size() == 4
