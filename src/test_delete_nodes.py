from __future__ import unicode_literals


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
