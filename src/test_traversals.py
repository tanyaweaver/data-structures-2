#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from bst import Node, Bst
import pytest
from conftest import BST_15, LIST_30, BST_7, BST_5_LEFT


DEPTH_PRE_ORDER = [10, 5, 2, 1, 3, 7, 6, 8, 9, 15, 12, 11, 13, 20, 18, 22]
DEPTH_IN_ORDER = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20, 22]
DEPTH_POST_ORDER = [1, 3, 2, 6, 9, 8, 7, 5, 11, 13, 12, 18, 22, 20, 15, 10]
BST_7_PRE = [15, 5, 14, 13, 11, 12, 20]


def test_traverse_breadth_empty():
    with pytest.raises(ValueError):
        bst = Bst()
        bst.breadth_tr()


def test_breadth1(bst_15):
    result = bst_15.breadth_tr()
    for x in result:
        assert x.value in BST_15


def test_breadth2(bst_list_30):
    result = bst_list_30.breadth_tr()
    for x in result:
        assert x.value in LIST_30


def test_breadth3(bst_7):
    result = bst_7.breadth_tr()
    for x in result:
        assert x.value in BST_7


def test_traverse_empty_post_order_tr(bst_empty):
    with pytest.raises(ValueError):
        bst_empty.depth_pre_order_tr()


def test_depth_pre_order1(bst_5_left):
    result = bst_5_left.depth_pre_order_tr()
    for x in result:
        assert x.value in BST_5_LEFT


def test_depth_pre_order2(bst_15):
    result = bst_15.depth_pre_order_tr()
    for x in result:
        assert x.value in DEPTH_PRE_ORDER


def test_depth_pre_order3(bst_7):
    result = bst_7.depth_pre_order_tr()
    for x in result:
        assert x.value in BST_7_PRE


def test_depth_in_order1(bst_15):
    result = bst_15.depth_in_order_tr()
    for x in result:
        assert x.value in DEPTH_IN_ORDER


def test_depth_post_order1(bst_15):
    result = bst_15.depth_post_order_tr()
    for x in result:
        assert x.value in DEPTH_POST_ORDER

