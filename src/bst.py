#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
import random
from collections import deque


class Node(object):
    """Define class for a node of a binary search tree."""

    def __init__(self, val):
        """Create an instance of Node."""
        self.value = val
        self.left = None
        self.right = None
        self.depth = 1

    def find_depth(self):
        """Find depth property of a node."""
        if self.left is not None:
            left_depth = self.left.depth
        else:
            left_depth = 0
        if self.right is not None:
            right_depth = self.right.depth
        else:
            right_depth = 0
        self.depth = 1 + max(left_depth, right_depth)
        return self.depth

    def _insert_node(self, new_node):
        """Insert a new node. <new_node> must be an instance of Node."""
        parent = self
        visited_nodes = [self]
        while True:
            if parent.value == new_node.value:
                break
            if new_node.value > parent.value:
                if parent.right is None:
                    parent.right = new_node
                    while len(visited_nodes) != 0:
                        visited_node = visited_nodes.pop()
                        visited_node.depth = visited_node.find_depth()
                    break
                else:
                    parent = parent.right
                    visited_nodes.append(parent)
            elif new_node.value < parent.value:
                if parent.left is None:
                    parent.left = new_node
                    while len(visited_nodes) != 0:
                        visited_node = visited_nodes.pop()
                        visited_node.depth = visited_node.find_depth()
                    break
                else:
                    parent = parent.left
                    visited_nodes.append(parent)

    def _compare_nodes(self, n2):
        """Compare two nodes. Return False if values of 2 nodes are
        not equal; return True otherwise."""
        parent = n2
        if self.value != parent.value:
            if self.value > parent.value:
                if parent.right is None:
                    return False
                else:
                    parent = parent.right
                    return self._compare_nodes(parent)
            elif self.value < parent.value:
                if parent.left is None:
                    return False
                else:
                    parent = parent.left
                    return self._compare_nodes(parent)
        else:
            return True


class Bst(object):
    """Define binary search tree class."""

    def __init__(self, iterable=None):
        """
        Create an instance of binary search tree.
        """
        self.head = None
        self.counter = 0
        if iterable is not None:
            try:
                for item in iterable:
                    self.insert(item)
            except TypeError:
                self.insert(iterable)

    def insert(self, value):
        """
        Insert the value into bst. If value is already present,
        it will be ignored.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.head._insert_node(new_node)
        self.counter += 1

    def contains(self, value):
        """
        Returns True if the value in the bst, False if not.
        """
        new_node = Node(value)
        if self.head is None:
            return False
        else:
            if new_node._compare_nodes(self.head):
                return True
            else:
                return False

    def size(self):
        """
        Return the integer size of the bst.
        Return zero if the bst is empty.
        """
        return self.counter

    def depth(self):
        """
        Return an integer representing the total levels in a tree.
        """
        return self.head.depth

    def balance(self):
        """
        Return an integer that represents how well balanced the tree is:
        - a positive value if the tree is higher on the left than the right;
        - a negative value if the tree is higher on the right than the left;
        - zero if the tree is ideally-balanced.
        """
        if self.head is None:
            return 0
        if self.head.left is not None:
            left_depth = self.head.left.depth
        else:
            left_depth = 0
        if self.head.right is not None:
            right_depth = self.head.right.depth
        else:
            right_depth = 0
        return left_depth - right_depth

        def gv(self):
            return self.head.get_dot

    def breadth_tr(self):
        if self.head is None:
            yield None
        current_node = self.head
        pending = deque([current_node])
        while len(pending) != 0:
            current_node = pending.pop()
            yield current_node
            if current_node.left is not None:
                pending.appendleft(current_node.left)
            if current_node.right is not None:
                pending.appendleft(current_node.right)

    def depth_pre_order_tr(self):
        if self.head is None:
            yield None
        current_node = self.head
        pending = deque([current_node])
        while len(pending) != 0:
            current_node = pending.pop()
            yield current_node
            if current_node.right is not None:
                pending.append(current_node.right)
            if current_node.left is not None:
                pending.append(current_node.left)








if __name__ == '__main__':

    import time

    bst1 = Bst([10, 5, 15, 2, 8, 12, 18, 1, 0, 3, 4, 6, 9,
                11, 13, 15, 16, 17, 20, 19, 20])
    bst2 = Bst(list(range(1, 21)))
    start_time_bst1 = time.time()
    searc_bst1 = bst1.contains(20)
    end_time_bst1 = time.time()
    time_bst1 = end_time_bst1 - start_time_bst1

    start_time_bst2 = time.time()
    searc_bst2 = bst2.contains(20)
    end_time_bst2 = time.time()
    time_bst2 = end_time_bst2 - start_time_bst2
    print('To find the biggest number in a binary search tree with {} nodes,'
          'it takes: {} - if the tree has depth 0f {},'
          'and {} - if the tree has depth of {}'
          .format(bst1.size(), time_bst1, bst1.depth(),
                  time_bst2, bst2.depth()))
