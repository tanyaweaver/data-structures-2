#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals


class Node(object):
    """Define class for a node of a binary search tree."""
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def compare_self_to_a_node(self, n2):
        """Assume n1 and n2 are instances of Node."""
        parent = n2
        if self.value != parent.value:
            if self.value > parent.value:
                if parent.right is None:
                    parent.right = self
                else:
                    parent = parent.right
                    self.compare_self_to_a_node(parent)
            elif self.value < parent.value:
                if parent.left is None:
                    parent.left = self
                else:
                    parent = parent.left
                    self.compare_self_to_a_node(parent)


class Bst(object):
    """Define binary search tree class."""
    def __init__(self, iterable=None):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.compare_self_to_a_node(self.head)
