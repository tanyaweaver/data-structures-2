#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from bst import Node, Bst


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
