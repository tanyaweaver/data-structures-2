#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from bst import Node, Bst
import pytest


@pytest.fixture(scope='function')
def node():
    """Create a node."""
    node = Node(3)
    return node


@pytest.fixture(scope='function')
def bst_empty():
    """Create an empty bst."""
    bst = Bst()
    return bst


@pytest.fixture(scope='function')
def bst_3():
    """Create a balanced bst with 3 nodes."""
    bst = Bst([10, 5, 15])
    bst.node_left = bst.head.left
    bst.node_right = bst.head.right
    return bst

BST_15 = [10, 5, 15, 2, 7, 12, 20, 1, 3, 6, 8, 11, 13, 18, 22, 9]
BST_7 = [15, 5, 20, 14, 13, 11, 12]
BST_5_LEFT = [5, 4, 3, 2, 1]
LIST_30 = list(range(30))


@pytest.fixture(scope='function')
def bst_5_left():
    """Create a tree with 5 nodes, depth = 5."""
    bst = Bst(BST_5_LEFT)
    return bst


@pytest.fixture(scope='function')
def bst_15():
    """Create a balanced bst with 3 nodes."""
    bst = Bst(BST_15)
    return bst


@pytest.fixture(scope='function')
def bst_7():
    """Create a balanced bst with 3 nodes."""
    bst = Bst(BST_7)
    return bst


@pytest.fixture(scope='function')
def bst_list_30():
    """Create a balanced bst with 3 nodes."""
    bst_list_30 = Bst(LIST_30)
    return bst_list_30
