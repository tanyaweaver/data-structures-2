from __future__ import unicode_literals
from bst import Bst
import pytest

BALANCE_3 = [
    # ([30, 20, 25], [25, 20, 30]),
    # ([30, 40, 35], [35, 30, 40]),
    # ([30, 20, 40, 45, 50], [40, 30, 45, 20, 50]),
    # ([30, 20, 40, 38, 37], [37, 30, 38, 20, 40]),
    # ([30, 40, 20, 15, 10], [20, 15, 30, 10, 40]),
    # ([30, 40, 20, 22, 25], [25, 22, 30, 20, 40]),
    ([10, 5, 15, 2, 7, 12, 20, 1, 3, 6, 8, 9],
     [7, 5, 10, 2, 6, 9, 15, 1, 3, 8, 12, 20])
]


@pytest.mark.parametrize('iterable, breadth_tr', BALANCE_3)
def test_self_balance3(iterable, breadth_tr):
    bst = Bst(iterable)
    bst._self_balance()
    result = []
    for x in bst.breadth_first():
        result.append(x)
    assert result == breadth_tr



# BALANCE_NONE = [
#     ([]),
#     ([1]),
#     ([10, 5, 15])
# ]


# @pytest.mark.parametrize('iterable', BALANCE_NONE)
# def test_self_balance1(iterable):
#     """
#     Prove that nothing happens if one of the following is true:
#     node is None, node.parent is None, node.parent.parent is None.
#     (No self-balancing is performed when bst.depth() < 3).
#     """
#     bst = Bst(iterable)
#     assert bst._self_balance(bst.head) is None

# BALANCED = [
#     ([30, 20, 25], 25, [25, 20, 30]),
#     ([30, 40, 35], 35, [35, 30, 40]),
#     ([30, 20, 40, 45, 50], 50, [30, 20, 45, 40, 50]),
#     ([30, 20, 40, 45, 43], 43, [30, 20, 43, 40, 45]),
#     ([30, 40, 20, 15, 10], 10, [30, 15, 40, 10, 20]),
#     ([30, 40, 20, 15, 17], 17, [30, 17, 40, 15, 20])
# ]
#
#
# @pytest.mark.parametrize('iterable, val, breadth_tr', BALANCED)
# def test_self_balance2(iterable, val, breadth_tr):
#     bst = Bst(iterable)
#     node = bst.return_node(val)
#     bst._self_balance(node)
#     result = []
#     for x in bst.breadth_first():
#         result.append(x)
#     assert result == breadth_tr


# LEFT_ROT = [
#     ([10, 5, 15, 2, 7, 12, 20, 1, 3, 6, 8, 9],
#      [10, 7, 15, 6, 8, 12, 20, 5, 9, 2, 1, 3])
# ]
#
#
# @pytest.mark.parametrize('iterable, breadth', LEFT_ROT)
# def test_rotate_left11(iterable, breadth):
#     bst = Bst(iterable)
#     result = []
#     node1 = bst.return_node(7)
#     node2 = bst.return_node(5)
#     bst.left_rotation(node1, node2)
#     for x in bst.breadth_first():
#         result.append(x)
#     assert result == breadth
#
#
# RIGHT_ROT = [
#     ([10, 7, 15, 6, 8, 12, 20, 5, 9, 2, 1, 3],
#      [7, 6, 8, 5, 9, 2, 10, 1, 3, 15, 12, 20])
# ]


# @pytest.mark.parametrize('iterable, breadth', RIGHT_ROT)
# def test_rotate_right12(iterable, breadth):
#     bst = Bst(iterable)
#     result = []
#     node1 = bst.return_node(7)
#     node2 = bst.return_node(10)
#     bst.right_rotation(node1, node2)
#     for x in bst.breadth_first():
#         result.append(x)
#     assert result == breadth

# def in_order_tr(bst):
#     lst = []
#     for x in bst.in_order():
#         lst.append(x)
#     return lst
#
#
# def breadth_traversal(bst):
#     lst = []
#     for x in bst.breadth_first():
#         lst.append(x)
#     return lst


# def test_balance_node1():
#     bst = Bst([10, 20, 30])
#     assert bst.return_node(20)._balance() == -1
#
#
# def test_balance_node2():
#     bst = Bst([10, 20, 30])
#     assert bst.return_node(10)._balance() == -2
#
#
# def bst_left_rotation(iterable, val1, val2):
#     bst = Bst(iterable)
#     node1 = bst.return_node(val1)
#     node2 = bst.return_node(val2)
#     bst.left_rotation(node1, node2)
#     return (bst, node1, node2)
#
#
# def bst_right_rotation(iterable, val1, val2):
#     bst = Bst(iterable)
#     node1 = bst.return_node(val1)
#     node2 = bst.return_node(val2)
#     bst.right_rotation(node1, node2)
#     return (bst, node1, node2)
#
#
# def test_rotate_left1():
#     """
#     Prove that left_rotation() doesn't change size of a tree.
#     """
#     bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
#     assert bst.size() == 3
#
#
# def test_rotate_left2():
#     """
#     Prove that after left_rotation() the tree has a right head.
#     """
#     bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
#     assert bst.head.value == 20
#
#
# def test_rotate_left3():
#     """
#     Prove that the tree has an expected depth after a left_rotation.
#     """
#     bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
#     assert bst.depth() == 2
#
#
# def test_rotate_left4():
#     """
#     Prove that the pivot node has the corrrect left child.
#     """
#     bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
#     assert node1.left.value == 10
#
#
# def test_rotate_left5():
#     """
#     Prove that the pivot node has the corrrect right child.
#     """
#     bst, node1, node2 = bst_left_rotation([10, 20, 30], 20, 10)
#     assert node1.right.value == 30
#
#
# def test_rotate_left6():
#     """
#     Prove that left_rotation() doesn't change size of a tree.
#     """
#     bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
#     assert bst.size() == 4
#
#
# def test_rotate_left7():
#     """
#     Prove that after left_rotation() the tree has a right head.
#     """
#     bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
#     assert bst.head.value == 5
#
#
# def test_rotate_left8():
#     """
#     Prove that the tree has an expected depth after a left_rotation.
#     """
#     bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
#     assert bst.depth() == 3
#
#
# def test_rotate_left9():
#     """
#     Prove that the pivot node has the corrrect left child.
#     """
#     bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
#     assert node1.left.value == 10
#
#
# def test_rotate_left10():
#     """
#     Prove that the pivot node has the corrrect right child.
#     """
#     bst, node1, node2 = bst_left_rotation([5, 10, 20, 30], 20, 10)
#     assert node1.right.value == 30
#
#
# def test_rotate_right1():
#     """
#     Prove that right_rotation() doesn't change size of a tree.
#     """
#     bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
#     assert bst.size() == 3
#
#
# def test_rotate_right2():
#     """
#     Prove that after right_rotation() the tree has a right head.
#     """
#     bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
#     assert bst.head.value == 20
#
#
# def test_rotate_right3():
#     """
#     Prove that the tree has an expected depth after a right_rotation.
#     """
#     bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
#     assert bst.depth() == 2
#
#
# def test_rotate_right4():
#     """
#     Prove that the pivot node has the corrrect right child.
#     """
#     bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
#     assert node1.right.value == 30
#
#
# def test_rotate_right5():
#     """
#     Prove that the pivot node has the corrrect left child.
#     """
#     bst, node1, node2 = bst_right_rotation([30, 20, 10], 20, 30)
#     assert node1.left.value == 10
#
#
# def test_rotate_right6():
#     """
#     Prove that right_rotation() doesn't change size of a tree.
#     """
#     bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
#     assert bst.size() == 4
#
#
# def test_rotate_right7():
#     """
#     Prove that after right_rotation() the tree has a right head.
#     """
#     bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
#     assert bst.head.value == 40
#
#
# def test_rotate_right8():
#     """
#     Prove that the tree has an expected depth after a right_rotation.
#     """
#     bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
#     assert bst.depth() == 3
#
#
# def test_rotate_right9():
#     """
#     Prove that the pivot node has the corrrect left child.
#     """
#     bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
#     assert node1.left.value == 10
#
#
# def test_rotate_right10():
#     """
#     Prove that the pivot node has the corrrect right child.
#     """
#     bst, node1, node2 = bst_right_rotation([40, 30, 20, 10], 20, 30)
#     assert node1.right.value == 30
