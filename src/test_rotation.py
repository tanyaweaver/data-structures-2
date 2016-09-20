from __future__ import unicode_literals
from bst import Bst


def in_order_tr(bst):
    lst = []
    for x in bst.in_order():
        lst.append(x)
    return lst


def breadth_traversal(bst):
    lst = []
    for x in bst.breadth_first():
        lst.append(x)
    return lst


def test_balance_node1():
    bst = Bst([10, 20, 30])
    assert bst.return_node(20)._balance() == -1


def test_balance_node2():
    bst = Bst([10, 20, 30])
    assert bst.return_node(10)._balance() == -2


def test_rotate_left():
    bst = Bst([10, 20, 30])
    bst.return_node(30).left_rotation()
    assert breadth_traversal(bst) == [20, 10, 30]
