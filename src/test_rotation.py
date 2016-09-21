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


def bst_left_rotation(iterable, val1, val2):
    bst = Bst(iterable)
    node1 = bst.return_node(val1)
    node2 = bst.return_node(val2)
    bst.left_rotation(node1, node2)
    return (bst, node1, node2)


def bst_right_rotation(iterable, val1, val2):
    bst = Bst(iterable)
    node1 = bst.return_node(val1)
    node2 = bst.return_node(val2)
    bst.right_rotation(node1, node2)
    return (bst, node1, node2)


def test_rotate_left1():
    """
    Prove that left_rotation() doesn't change size of a tree.
    """
    bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
    assert bst.size() == 3


def test_rotate_left2():
    """
    Prove that after left_rotation() the tree has a right head.
    """
    bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
    assert bst.head.value == 20


def test_rotate_left3():
    """
    Prove that the tree has an expected depth after a left_rotation.
    """
    bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
    assert bst.depth() == 2


def test_rotate_left4():
    """
    Prove that the pivot node has the corrrect left child.
    """
    bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
    assert node1.left.value == 10


def test_rotate_left5():
    """
    Prove that the pivot node has the corrrect right child.
    """
    bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
    assert node1.right.value == 30


def test_rotate_left6():
    """
    Prove that left_rotation() doesn't change size of a tree.
    """
    bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
    assert bst.size() == 4


def test_rotate_left7():
    """
    Prove that after left_rotation() the tree has a right head.
    """
    bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
    assert bst.head.value == 5


def test_rotate_left8():
    """
    Prove that the tree has an expected depth after a left_rotation.
    """
    bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
    assert bst.depth() == 3


def test_rotate_left9():
    """
    Prove that the pivot node has the corrrect left child.
    """
    bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
    assert node1.left.value == 10


def test_rotate_left10():
    """
    Prove that the pivot node has the corrrect right child.
    """
    bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
    assert node1.right.value == 30


def test_rotate_right1():
    """
    Prove that right_rotation() doesn't change size of a tree.
    """
    bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
    assert bst.size() == 3


def test_rotate_right2():
    """
    Prove that after right_rotation() the tree has a right head.
    """
    bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
    assert bst.head.value == 20


def test_rotate_right3():
    """
    Prove that the tree has an expected depth after a right_rotation.
    """
    bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
    assert bst.depth() == 2


def test_rotate_right4():
    """
    Prove that the pivot node has the corrrect right child.
    """
    bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
    assert node1.right.value == 30


def test_rotate_right5():
    """
    Prove that the pivot node has the corrrect left child.
    """
    bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
    assert node1.left.value == 10


def test_rotate_right6():
    """
    Prove that right_rotation() doesn't change size of a tree.
    """
    bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
    assert bst.size() == 4


def test_rotate_right7():
    """
    Prove that after right_rotation() the tree has a right head.
    """
    bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
    assert bst.head.value == 40


def test_rotate_right8():
    """
    Prove that the tree has an expected depth after a right_rotation.
    """
    bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
    assert bst.depth() == 3


def test_rotate_right9():
    """
    Prove that the pivot node has the corrrect left child.
    """
    bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
    assert node1.left.value == 10


def test_rotate_right10():
    """
    Prove that the pivot node has the corrrect right child.
    """
    bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
    assert node1.right.value == 30
