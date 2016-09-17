#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from bst import Node, Bst
import pytest


def test_node_init_value(node):
    """
    Test that a new instance of Node(value) has self.value == value.
    """
    assert node.value == 3


def test_node_init_selfleft(node):
    """
    Test that a new instance of Node(value) has self.left == None.
    """
    assert node.left is None


def test_node_init_selfright(node):
    """
    Test that a new instance of Node(value) has self.right == None.
    """
    assert node.right is None


def test_node_init_depth(node):
    """
    Test that a new instance of Node(value) has self.depth == 1.
    """
    assert node.depth == 1


def test_node_init_parent(node):
    """
    Test that a new instance of Node(value) self.parent is None.
    """
    assert node.parent is None


def test_compare_self_to_a_bigger_node1(node):
    """
    Test that function _insert_node(self, n)
    assigns n.left = self.value if self.value is smaller than n.value.
    """
    node2 = Node(5)
    node2._insert_node(node)
    assert node2.left.value == 3


def test_compare_self_to_a_bigger_node2(node):
    """
    Test that function _insert_node(self, n)
    doesn't change n.right = None if self.value is smaller than n.value.
    """
    node2 = Node(5)
    node2._insert_node(node)
    assert node2.right is None


def test_compare_self_to_a_smaller_node1(node):
    """
    Test that function _insert_node(self, n)
    assigns n.right = self.value if self.value is bigger than n.value.
    """
    node1 = Node(7)
    node._insert_node(node1)
    assert node.right.value == 7


def test_compare_self_to_a_smaller_node2(node):
    """
    Test that function _insert_node(self, n)
    doesn't change n.left = None if self.value is bigger than n.value.
    """
    node1 = Node(7)
    node._insert_node(node1)
    assert node.left is None


def test_compare_self_to_equal_value1(node):
    """
    Test that function _insert_node(self, n)
    doesn't change n.left = None if self.value is equal to n.value.
    """
    node1 = Node(3)
    node._insert_node(node1)
    assert node.left is None


def test_compare_self_to_equal_value2(node):
    """
    Test that function _insert_node(self, n)
    doesn't change n.right = None if self.value is equal to n.value.
    """
    node1 = Node(3)
    node._insert_node(node1)
    assert node.right is None


def test_bst_init():
    """
    Test that a new instance of Bst has approprite self.head value.
    """
    bst = Bst()
    assert bst.head is None


def test_insert(bst_empty):
    """
    Test whether head has appropriate value after inserting
    a node into an empty bst.
    """
    bst_empty.insert(5)
    assert bst_empty.head.value == 5


def test_insert_left1(bst_empty):
    """
    Test whether head.left has appropriate value after inserting
    2 nodes into an empty bst.
    """
    bst_empty.insert(5)
    bst_empty.insert(1)
    assert bst_empty.head.left.value == 1


def test_insert_right1(bst_empty):
    """
    Test whether head.right has appropriate value after inserting
    2 nodes into an empty bst.
    """
    bst_empty.insert(5)
    bst_empty.insert(10)
    assert bst_empty.head.right.value == 10


def test_insert_left_left(bst_3):
    """
    Test whether a node is inserted appropriately in a bst with 3 nodes.
    """
    bst_3.insert(2)
    assert bst_3.node_left.left.value == 2


def test_insert_left_right(bst_3):
    """
    Test whether a node is inserted appropriately in a bst with 3 nodes.
    """
    bst_3.insert(7)
    assert bst_3.node_left.right.value == 7


def test_insert_right_left(bst_3):
    """
    Test whether a node is inserted appropriately in a bst with 3 nodes.
    """
    bst_3.insert(12)
    assert bst_3.node_right.left.value == 12


def test_insert_right_right(bst_3):
    """
    Test whether a node is inserted appropriately in a bst with 3 nodes.
    """
    bst_3.insert(17)
    assert bst_3.node_right.right.value == 17


def test_insert_parent1(bst_3):
    bst_3.insert(17)
    assert bst_3.node_right.right.parent.value == 15


def test_insert_parent2(bst_3):
    assert bst_3.node_right.parent.value == 10


def test_contains_true5(bst_3):
    """
    Test whether contains() returns True if node exists.
    """
    assert bst_3.contains(5) is True


def test_contains_true15(bst_3):
    """
    Test whether contains() returns True if node exists.
    """
    assert bst_3.contains(15) is True


def test_contains_true10(bst_3):
    """
    Test whether contains() returns True if node exists.
    """
    assert bst_3.contains(10) is True


def test_contains_false(bst_3):
    """
    Test whether contains() returns False if node doesn't exist.
    """
    assert bst_3.contains(6) is False


def test_contains_empty(bst_empty):
    """
    Test whether contains() returns True if node exists.
    """
    assert bst_empty.contains(5) is False


def test_size_empty(bst_empty):
    """
    Test whether size() returns 0 for an empty bst.
    """
    assert bst_empty.size() == 0


def test_size_3(bst_3):
    """
    Test whether size() returns 3 for a bst with 3 nodes.
    """
    assert bst_3.size() == 3


def test_size_4(bst_3):
    """
    Test whether size() returns an expected value after inserting a node.
    """
    bst_3.insert(18)
    assert bst_3.size() == 4


def test_depth_node_insert1(node):
    """
    Test whether node.depth is correct after node.insert().
    """
    node._insert_node(Node(5))
    assert node.depth == 2


def test_depth_node_insert2(node):
    """
    Test whether node.depth is correct after node.insert().
    """
    node._insert_node(Node(5))
    node._insert_node(Node(4))
    assert node.depth == 3


def test_depth_node_insert4(node):
    """
    Test whether node.depth is correct after node.insert().
    """
    node._insert_node(Node(5))
    node._insert_node(Node(4))
    node._insert_node(Node(8))
    node._insert_node(Node(7))
    assert node.depth == 4


def test_depth_node_insert5(node):
    """
    Test whether node.depth is correct after node.insert().
    """
    node._insert_node(Node(5))
    node._insert_node(Node(4))
    node._insert_node(Node(8))
    node._insert_node(Node(7))
    node._insert_node(Node(6))
    assert node.depth == 5


def test_depth_tree_insert1(bst_empty):
    """
    Test whether bst.depth() returns appropriate depth.
    """
    bst_empty.insert(5)
    assert bst_empty.depth() == 1


def test_depth_tree_insert2(bst_empty):
    """
    Test whether bst.depth() returns appropriate depth.
    """
    bst_empty.insert(4)
    bst_empty.insert(5)
    assert bst_empty.depth() == 2


def test_depth_tree_insert3(bst_empty):
    """
    Test whether bst.depth() returns appropriate depth.
    """
    bst_empty.insert(4)
    bst_empty.insert(5)
    bst_empty.insert(6)
    assert bst_empty.depth() == 3


def test_balance_empty(bst_empty):
    """
    Test whether bst.balance() returns appropriate value.
    """
    assert bst_empty.balance() == 0


def test_balance_2_neg(bst_empty):
    """
    Test whether bst.balance() returns appropriate value.
    """
    bst_empty.insert(5)
    bst_empty.insert(7)
    assert bst_empty.balance() < 0


def test_balance_2_pos(bst_empty):
    """
    Test whether bst.balance() returns appropriate value.
    """
    bst_empty.insert(5)
    bst_empty.insert(4)
    assert bst_empty.balance() > 0


def test_balance_3_balanced(bst_3):
    """
    Test whether bst.balance() returns appropriate value.
    """
    assert bst_3.balance() == 0

INSERT_BALANCE = [
    [7, 4], [20, 13], [(4, 20)]
]


@pytest.mark.parametrize('val', INSERT_BALANCE[0])
def test_balance_pos(val, bst_3):
    """
    Test whether bst.balance() returns appropriate value.
    """
    bst_3.insert(val)
    assert bst_3.balance() > 0


@pytest.mark.parametrize('val', INSERT_BALANCE[1])
def test_balance_neg(val, bst_3):
    """
    Test whether bst.balance() returns appropriate value.
    """
    bst_3.insert(val)
    assert bst_3.balance() < 0


@pytest.mark.parametrize('val1, val2', INSERT_BALANCE[2])
def test_balance_balanced(val1, val2, bst_3):
    """
    Test whether bst.balance() returns appropriate value.
    """
    bst_3.insert(val1)
    bst_3.insert(val2)
    assert bst_3.balance() == 0

IT_DEPTH = [
    ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 10),
    ((6, 7, 8, 9, 10, 1, 2, 3, 4, 5), 6),
    ((10, 2, 13, 4, 15, 6, 27, 18, 9, 10), 5),
    ((1286547), 1)
]


@pytest.mark.parametrize('iterable, depth', IT_DEPTH)
def test_init_iterable(iterable, depth):
    """
    Test whether bst has the expected depth after initiation
    with an iterable.
    """
    bst = Bst(iterable)
    assert bst.depth() == depth
