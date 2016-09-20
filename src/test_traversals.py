# #!/usr/bin/env python
# # -*- coding: utf -8 -*-

# from __future__ import unicode_literals
# from conftest import BST_15, LIST_30, BST_7, BST_5_LEFT


# DEPTH_PRE_ORDER = [10, 5, 2, 1, 3, 7, 6, 8, 9, 15, 12, 11, 13, 20, 18, 22]
# DEPTH_IN_ORDER = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20, 22]
# DEPTH_POST_ORDER = [1, 3, 2, 6, 9, 8, 7, 5, 11, 13, 12, 18, 22, 20, 15, 10]
# BST_7_PRE = [15, 5, 14, 13, 11, 12, 20]
# BST_7_IN = [5, 11, 12, 13, 14, 15, 20]
# BST_7_POST = [12, 11, 13, 14, 5, 20, 15]
# BST_5_IN_POST = [1, 2, 3, 4, 5]


# def test_traverse_breadth_empty(bst_empty):
#     """Test breadth traversal on empty tree returns None."""
#     for x in bst_empty.breadth_first():
#         assert x is None


# def test_traverse_pre_empty(bst_empty):
#     """Test pre-order traversal on empty tree returns None."""
#     for x in bst_empty.pre_order():
#         assert x is None


# def test_traverse_in_empty(bst_empty):
#     """Test in-order traversal on empty tree returns None."""
#     for x in bst_empty.in_order():
#         assert x is None


# def test_traverse_empty_post_order_tr(bst_empty):
#     """Test post-order traversal on empty tree returns None."""
#     bst_empty.post_order()
#     for x in bst_empty.post_order():
#         assert x is None


# def test_breadth1(bst_15):
#     """Test that breadth_first() returns appropriate values.
#     """
#     result = bst_15.breadth_first()
#     for x in result:
#         assert x in BST_15


# def test_breadth2(bst_list_30):
#     """Test that breadth_first() returns appropriate values.
#     """
#     result = bst_list_30.breadth_first()
#     for x in result:
#         assert x in LIST_30


# def test_breadth3(bst_7):
#     """Test that breadth_first() returns appropriate values.
#     """
#     result = bst_7.breadth_first()
#     for x in result:
#         assert x in BST_7


# def test_depth_pre_order1(bst_5_left):
#     """Test that depth pre-order traversal returns appropriate values.
#     """
#     result = bst_5_left.pre_order()
#     for x in result:
#         assert x in BST_5_LEFT


# def test_depth_pre_order2(bst_15):
#     """Test that depth pre-order traversal returns appropriate values.
#     """
#     result = bst_15.pre_order()
#     for x in result:
#         assert x in DEPTH_PRE_ORDER


# def test_depth_pre_order3(bst_7):
#     """Test that depth pre-order traversal returns appropriate values.
#     """
#     result = bst_7.pre_order()
#     for x in result:
#         assert x in BST_7_PRE


# def test_depth_in_order1(bst_15):
#     """Test that depth in-order traversal returns appropriate values.
#     """
#     result = bst_15.in_order()
#     for x in result:
#         assert x in DEPTH_IN_ORDER


# def test_depth_post_order1(bst_15):
#     """Test that depth post order traversal returns appropriate values.
#     """
#     result = bst_15.post_order()
#     for x in result:
#         assert x in DEPTH_POST_ORDER


# def test_depth_in_order2(bst_7):
#     """Test that depth in order traversal returns appropriate values.
#     """
#     result = bst_7.in_order()
#     for x in result:
#         assert x in BST_7_IN


# def test_depth_post_order2(bst_7):
#     """Test that depth post order traversal returns appropriate values.
#     """
#     result = bst_7.post_order()
#     for x in result:
#         assert x in BST_7_POST


# def test_depth_in_order3(bst_5_left):
#     """Test that depth in order traversal returns appropriate values.
#     """
#     result = bst_5_left.in_order()
#     for x in result:
#         assert x in BST_5_IN_POST


# def test_depth_post_order3(bst_5_left):
#     """Test that depth post order traversal returns appropriate values.
#     """
#     result = bst_5_left.post_order()
#     for x in result:
#         assert x in BST_5_IN_POST
