from __future__ import unicode_literals
from bst import Bst
import pytest


NODE_BALANCE = [
    ([10, 20, 30], 20, -1),
    ([10, 20, 30], 10, -2),
    ([20, 10, 30, 5, 16, 25, 11, 13], 20, 2),
    ([10, 7, 15, 6, 8, 12, 20, 5, 9, 2, 1, 3], 10, 3)
]


@pytest.mark.parametrize('iterable, val, balance', NODE_BALANCE)
def test_balance_node(iterable, val, balance):
    """
    Prove that ._balance() returns an expected balance of a node.
    """
    bst = Bst(iterable=iterable, self_balance=False)
    node = bst.return_node(val)
    assert node._balance() == balance


LEFT_ROT = [
    ([10, 20, 30], 20, 10, [20, 10, 30]),
    ([5, 10, 20, 30], 20, 10, [5, 20, 10, 30]),
    ([10, 5, 15, 2, 7, 12, 20, 1, 3, 6, 8, 9], 7, 5,
     [10, 7, 15, 6, 8, 12, 20, 5, 9, 2, 1, 3]),
]


@pytest.mark.parametrize('iterable, val1, val2, breadth', LEFT_ROT)
def test_rotate_left(iterable, val1, val2, breadth):
    """
    Prove .left_rotation() results in the appropriate tree structure.
    Use breadth first traversal to access the resulted tree structure.
    """
    bst = Bst(iterable=iterable, self_balance=False)
    result = []
    node1 = bst.return_node(val1)
    node2 = bst.return_node(val2)
    bst.left_rotation(node1, node2)
    for x in bst.breadth_first():
        result.append(x)
    assert result == breadth


RIGHT_ROT = [
    ([40, 30, 20, 10], 20, 30, [40, 20, 10, 30]),
    ([10, 7, 15, 6, 8, 12, 20, 5, 9, 2, 1, 3], 7, 10,
     [7, 6, 8, 5, 9, 2, 10, 1, 3, 15, 12, 20]),
]


@pytest.mark.parametrize('iterable, val1, val2, breadth', RIGHT_ROT)
def test_rotate_right(iterable, val1, val2, breadth):
    """
    Prove .right_rotation() results in the appropriate tree structure.
    Use breadth first traversal to access the resulted tree structure.
    """
    bst = Bst(iterable=iterable, self_balance=False)
    result = []
    node1 = bst.return_node(val1)
    node2 = bst.return_node(val2)
    bst.right_rotation(node1, node2)
    for x in bst.breadth_first():
        result.append(x)
    assert result == breadth


SELF_BALANCE = [
    ([30, 20, 25], [25, 20, 30]),
    ([30, 40, 35], [35, 30, 40]),
    ([30, 20, 40, 45, 50], [40, 30, 45, 20, 50]),
    ([30, 20, 40, 38, 37], [37, 30, 38, 20, 40]),
    ([30, 40, 20, 15, 10], [20, 15, 30, 10, 40]),
    ([30, 40, 20, 22, 25], [25, 22, 30, 20, 40]),
    ([10, 5, 15, 2, 7, 12, 20, 1, 3, 6, 8, 9],
     [8, 5, 10, 2, 6, 9, 15, 1, 3, 7, 12, 20]),
    ([20, 10, 30, 5, 16, 25, 11, 13], [16, 11, 25, 10, 13, 20, 30, 5]),
]


@pytest.mark.parametrize('iterable, breadth_tr', SELF_BALANCE)
def test_self_balance3(iterable, breadth_tr):
    """
    Prove that ._self_balance() results in the appropriate tree structure.
    Use breadth first traversal to access the resulted tree structure.
    """
    bst = Bst(iterable=iterable, self_balance=False)
    bst._self_balance()
    result = []
    for x in bst.breadth_first():
        result.append(x)
    assert result == breadth_tr
