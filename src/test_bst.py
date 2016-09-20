#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from bst import Node, Bst
import pytest


def test_return_node1(bst_15):
    """Prove that returned node has the right value."""
    assert bst_15.return_node(1).value == 1


def test_return_node2(bst_15):
    """Prove that return_node returns False, when node is not in the tree."""
    assert bst_15.return_node(100) is False


def test_return_node3(bst_15):
    """Prove that returned node has the right value."""
    assert bst_15.return_node(22).value == 22


def test_return_node4(bst_15):
    """Prove that returned node has the right parent value."""
    assert bst_15.return_node(1).parent.value == 2

NEXT_BIGGER = [(10, 11), (15, 18), (12, 13)]


@pytest.mark.parametrize('node, next_bigger', NEXT_BIGGER)
def test_find_next_bigger1(node, next_bigger, bst_15):
    """Prove that returned node has the right value."""
    node = bst_15.return_node(node)
    assert node._find_next_bigger().value == next_bigger


def test_find_next_bigger3(bst_15):
    """Prove that function returns None if there is no next bigger child."""
    node = bst_15.return_node(22)
    assert node._find_next_bigger() is None

PREV_SMALLER = [(10, 9), (20, 18), (10, 9), (5, 3)]


@pytest.mark.parametrize('node, prev_smaller', PREV_SMALLER)
def test_find_previous_smaller(node, prev_smaller, bst_15):
    """Prove that returned node has the right value."""
    node = bst_15.return_node(node)
    assert node._find_previous_smaller().value == prev_smaller


def test_find_previous_smaller1(bst_15):
    """
    Prove that function returns None if there is no previous
    smaller child.
    """
    node = bst_15.return_node(22)
    assert node._find_previous_smaller() is None


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


def test_insert_the_child_into_a_node1():
    """
    Test that _insert_node(self, n)
    inserts n as the left child when n.value < self.value.
    """
    node = Node(5)
    node._insert_node(Node(3))
    assert node.left.value == 3


def test_insert_the_child_into_a_node2():
    """
    Test that _insert_node(self, n)
    assigns the right parent to the child.
    """
    node = Node(5)
    node._insert_node(Node(3))
    assert node.left.parent is node


def test_insert_the_child_into_a_node3():
    """
    Test that _insert_node(self, n)
    inserts n as the left child when n.value < self.value.
    """
    node = Node(3)
    node._insert_node(Node(2))
    assert node.right is None


def test_insert_the_child_into_a_node4():
    """
    Test that _insert_node(self, n)
    inserts n as the right child when n.value > self.value.
    """
    node = Node(3)
    node._insert_node(Node(7))
    assert node.right.value == 7


def test_insert_the_child_into_a_node5():
    """
    Test that _insert_node(self, n)
    inserts n as the right child when n.value > self.value.
    """
    node = Node(3)
    node._insert_node(Node(7))
    assert node.left is None


def test_insert_the_child_into_a_node6():
    """
    Test that _insert_node(self, n)
    doesn't insert a child if it already in the tree.
    """
    node = Node(3)
    node._insert_node(Node(3))
    assert node.left is None


def test_insert_the_child_into_a_node7(node):
    """
    Test that _insert_node(self, n)
    doesn't insert a child if it already in the tree.
    """
    node = Node(3)
    node._insert_node(Node(3))
    assert node.right is None


def test_insert_the_child_into_a_node8(node):
    """
    Test that _insert_node(self, n)
    doesn't insert a child if it already in the tree.
    """
    node = Node(3)
    node._insert_node(Node(3))
    assert node.depth == 1


def test_insert_the_child_into_a_node9(node):
    """
    Test that _insert_node(self, n)
    insert a child and adjusts the depth of the parent.
    """
    node = Node(3)
    node._insert_node(Node(5))
    assert node.depth == 2


def test_insert_the_child_into_a_node10(node):
    """
    Test that _insert_node(self, n)
    insert a child and adjusts the depth of the parent.
    """
    node = Node(3)
    node._insert_node(Node(2))
    assert node.depth == 2


def test_tree_insert_node1(bst_empty):
    """
    Test that function insert(self, n)
    assigns n.parent correctly when a node inserted into an empty bst.
    """
    bst_empty.insert(3)
    assert bst_empty.head.parent is None


def test_tree_insert_node2(bst_3):
    """
    Test that function insert(self, n) assigns n.parent correctly
    when a node inserted in the bst with 3 nodes.
    """
    bst_3.insert(3)
    assert bst_3.return_node(5).left.parent.value == 5


def test_tree_insert_node3(bst_3):
    """
    Test that function insert(self, n) ignores a node
    if it is already in the tree.
    """
    bst_3.insert(5)
    assert bst_3.size() == 3


def test_tree_insert_ignores_duplicate(bst_3):
    """
    Test that function insert(self, n) ignores a node
    if it is already in the tree.
    """
    bst_3.insert(5)
    list_in_order = []
    for x in bst_3.in_order():
        list_in_order.append(x)
    assert list_in_order == [5, 10, 15]


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
