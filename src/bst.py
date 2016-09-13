#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals


class Node(object):
    """Define class for a node of a binary search tree."""

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.depth = 1

    def compare_self_to_a_node(self, new_node):
        """Assume n1 and n2 are instances of Node."""
        parent = self
        current_depth = 0
        while True:
            if parent.value == new_node.value:
                break
            current_depth += 1
            if new_node.value > parent.value:
                parent.depth += 1
                if parent.right is None:
                    parent.right = new_node
                    parent.depth = max(parent.depth, current_depth)
                    break
                else:
                    parent = parent.right
            elif new_node.value < parent.value:
                parent.depth += 1
                if parent.left is None:
                    parent.left = new_node
                    break
                else:
                    parent = parent.left

    def compare_nodes(self, n2):
        """Assume n1 and n2 are instances of Node."""
        parent = n2
        if self.value != parent.value:
            if self.value > parent.value:
                if parent.right is None:
                    return False
                else:
                    parent = parent.right
                    return self.compare_nodes(parent)
            elif self.value < parent.value:
                if parent.left is None:
                    return False
                else:
                    parent = parent.left
                    return self.compare_nodes(parent)
        else:
            return True


class Bst(object):
    """Define binary search tree class."""

    def __init__(self, iterable=None):
        self.head = None
        self.counter = 0

    def insert(self, value):
        """
        Insert the value into bst. If value is already present,
        it will be ignored.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.head.compare_self_to_a_node(new_node)
        self.counter += 1

    def contains(self, value):
        """
        Returns True if the value in the bst, False if not.
        """
        new_node = Node(value)
        # import pdb; pdb.set_trace()
        if self.head is None:
            return False
        else:
            if new_node.compare_nodes(self.head):
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
        return self.depth
