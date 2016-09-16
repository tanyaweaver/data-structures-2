#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from bst import Node, Bst
import pytest
from conftest import BST_15, LIST_30


DEPTH_PRE_ORDER = [10, 5, 2, 1, 3, 7, 6, 8, 9, 15, 12, 11, 13, 20, 18, 22]
DEPTH_IN_ORDER = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20, 22]
DEPTH_POST_ORDER = [1, 3, 2, 6, 9, 8, 7, 5, 11, 13, 12, 18, 22, 20, 15, 10]


def test_breadth1(bst_15):
    result = bst_15.breadth_tr()
    for x in result:
        assert x.value in BST_15


def test_breadth2(bst_list_30):
    result = bst_list_30.breadth_tr()
    for x in result:
        assert x.value in LIST_30


def test_depth_pre_order1(bst_15):
    result = bst_15.depth_pre_order_tr()
    for x in result:
        assert x.value in DEPTH_PRE_ORDER


def test_depth_in_order1(bst_15):
    result = bst_15.depth_in_order_tr()
    for x in result:
        assert x.value in DEPTH_IN_ORDER


def test_depth_post_order1(bst_15):
    result = bst_15.depth_post_order_tr()
    for x in result:
        assert x.value in DEPTH_POST_ORDER


# def generator():
#     x = 5
#     while x > 0:
#         yield x
#         x -= 1


# def test_generator():
#     result = generator()
#     for x in result:
#         assert x in [1, 2, 3, 4, 5]