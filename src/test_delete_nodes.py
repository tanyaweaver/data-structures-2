from __future__ import unicode_literals
from bst import Bst


def test_delete_leaf1(bst_15):
    """
    Prove that after deletion of a leaf,
    the tree no longer has that leaf.
    """
    leaf = bst_15.return_node(1)
    leaf._delete_leaf()
    assert bst_15.contains(1) is False


def test_delete_leaf2(bst_15):
    """
    Prove that after deletion of a leaf,
    the tree has the right depth.
    """
    leaf = bst_15.return_node(1)
    leaf._delete_leaf()
    assert bst_15.depth() == 5


def test_delete_leaf3(bst_15):
    """
    Prove that after deletion of a leaf,
    the deleted node is no longer child of it's parent.
    """
    leaf = bst_15.return_node(1)
    leaf._delete_leaf()
    assert bst_15.return_node(2).left is None


def test_delete_leaf4(bst_15):
    """
    Prove that after deletion of a leaf,
    the tree has the right depth.
    """
    leaf = bst_15.return_node(9)
    leaf._delete_leaf()
    assert bst_15.depth() == 4


def test_delete_node_size1(bst_15):
    """
    Prove that after deletion of a node,
    the tree size is decreased by 1
    if node exsited in the tree.
    """
    before_size = bst_15.size()
    bst_15.delete(10)
    after_size = bst_15.size()
    assert before_size - 1 == after_size


def test_delete_node_size2(bst_15):
    """
    Prove that after deletion of a node,
    the tree size is  the same
    if node did not exist in the tree.
    """
    before_size = bst_15.size()
    bst_15.delete(100)
    after_size = bst_15.size()
    assert before_size == after_size


def test_delete_node_size3():
    """
    Prove that after deletion of a node
    from a tree with 1 node,
    the tree size is 0.
    """
    bst1 = Bst(1)
    before_size = bst1.size()
    bst1.delete(1)
    after_size = bst1.size()
    assert before_size - 1 == after_size


def test_delete_node_size4(bst_empty):
    """
    Prove that the size of an empty tree
    stays 0 when trying to delete a node.
    """
    bst_empty.delete(10)
    assert bst_empty.size() == 0


def test_delete_node_head1():
    """
    Prove that after deletion of a node
    from a tree with 1 node,
    the tree.head.value is None.
    """
    bst1 = Bst(1)
    bst1.delete(1)
    assert bst1.head is None


def test_delete_node1(bst_15):
    """
    Prove that after deletion of a node,
    the tree has the right depth.
    """
    bst_15.delete(10)
    assert bst_15.depth() == 4


def test_delete_node2(bst_15):
    """
    Prove that after deletion of a node,
    the tree has the right head.
    """
    bst_15.delete(10)
    assert bst_15.head.value == 9


def test_delete_node3(bst_15):
    """
    Prove that after deletion of a node,
    the tree no longer has that node.
    """
    bst_15.delete(10)
    assert bst_15.contains(10) is False


def test_delete_node4(bst_15):
    """
    Prove that after deletion of a node,
    the replacement node is no longer child of it's old parent.
    """
    bst_15.delete(10)
    assert bst_15.return_node(8).right is None


def test_delete_node5(bst_15):
    """
    Prove that after deletion of a node,
    the replacement node is no longer child of it's old parent.
    """
    bst_15.delete(5)
    assert bst_15.return_node(7).left is None


def test_delete_node6(bst_15):
    """
    Prove that after deletion of a node,
    the replacement node has the left child of the deleted node.
    """
    bst_15.delete(5)
    assert bst_15.return_node(6).left.value == 2


def test_delete_node7(bst_15):
    """
    Prove that after deletion of a node,
    the replacement node has the right child of the deleted node.
    """
    bst_15.delete(5)
    assert bst_15.return_node(6).right.value == 7


def test_delete_node8(bst_15):
    """
    Prove that after deletion of a node,
    the replacement node has the parent of the deleted node.
    """
    bst_15.delete(5)
    assert bst_15.return_node(6).parent.value == 10


def test_delete_node9(bst_15):
    """
    Prove that after deletion of a node,
    the parent of the deleted node has the replacement node as it's child.
    """
    bst_15.delete(5)
    assert bst_15.head.left.value == 6


def test_delete_node10(bst_15):
    """
    Prove that after deletion of a node,
    the tree has the appropriate depth.
    """
    bst_15.delete(5)
    assert bst_15.depth() == 5


def test_delete_nod11(bst_15):
    """
    Prove that after deletion of a node,
    the node is no longer in the tree.
    """
    bst_15.delete(5)
    assert bst_15.contains(5) is False


def test_delete_node12(bst_15):
    """
    Prove that after deletion of a node,
    the node is no longer in the tree.
    """
    bst_15.delete(9)
    assert bst_15.contains(9) is False


def test_delete_node13(bst_15):
    """
    Prove that after deletion of a node,
    the replacement node is no longer child of it's old parent.
    """
    bst_15.delete(9)
    assert bst_15.return_node(8).right is None


def test_delete_node14(bst_15):
    """
    Prove that nothing happens if node_to_delete is not in the tree.
    """
    assert bst_15.delete(100) is None


def test_delete_node15(bst_3):
    """
    Prove that the rest of the nodes are still present
    in a tree, after deletion of one node.
    """
    bst_3.delete(5)
    list_in_order = []
    for x in bst_3.in_order():
        list_in_order.append(x)
    assert list_in_order == [10, 15]


def test_delete_node16(bst_3):
    """
    Prove that all the nodes are still present
    in a tree, after trying to delete a node thatdoesn't
    exist in the tree.
    """
    bst_3.delete(555)
    list_in_order = []
    for x in bst_3.in_order():
        list_in_order.append(x)
    assert list_in_order == [5, 10, 15]
