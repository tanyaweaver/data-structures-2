from __future__ import unicode_literals
from bst import Node
from conftest import BST_15, LIST_30, BST_7, BST_5_LEFT

def test_delete_leaf(bst_15):
    bst_15.delete(1)
    assert bst_15.head.depth == 5


def test_delete_leaf2(bst_15):
    bst_15.delete(9)
    assert bst_15.head.depth == 4


def test_delete_leaf3(bst_15):
    bst_15.delete(9)
    assert bst_15.contains(9) is False


def test_delete_leaf4(bst_15):
    parent = Node(9)._compare_nodes(bst_15.head).parent
    bst_15.delete(9)
    assert parent.right is None


def test_delete_node1(bst_15):
    bst_15.delete(10)
    assert bst_15.depth() == 4


def test_delete_node2(bst_15):
    bst_15.delete(10)
    assert bst_15.head.value == 9


def test_delete_node3(bst_15):
    bst_15.delete(10)
    assert bst_15.contains(10) is False

def test_delete_node4(bst_15):
    bst_15.delete(10)
    parent = Node(8)._compare_nodes(bst_15.head)
    assert parent.right is None


def test_delete_node5(bst_15):
    bst_15.delete(5)
    parent = Node(7)._compare_nodes(bst_15.head)
    assert parent.left is None


def test_delete_node6(bst_15):
    bst_15.delete(5)
    parent = Node(6)._compare_nodes(bst_15.head)
    assert parent.left.value == 2


def test_delete_node7(bst_15):
    bst_15.delete(5)
    parent = Node(6)._compare_nodes(bst_15.head)
    assert parent.right.value == 7


def test_delete_node8(bst_15):
    bst_15.delete(5)
    parent = Node(6)._compare_nodes(bst_15.head)
    assert parent.parent.value == 10


def test_delete_node9(bst_15):
    bst_15.delete(5)
    assert bst_15.head.left.value == 6


def test_delete_node10(bst_15):
    bst_15.delete(5)
    assert bst_15.depth() == 5


def test_delete_nod11(bst_15):
    bst_15.delete(5)
    assert bst_15.contains(5) is False
