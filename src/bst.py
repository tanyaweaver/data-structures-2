#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from collections import deque


class Node(object):
    """Define class for a node of a binary search tree."""

    def __init__(self, val):
        """Create an instance of Node."""
        self.value = val
        self.left = None
        self.right = None
        self.depth = 1
        self.parent = None

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
                    new_node.parent = parent
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
                    new_node.parent = parent
                    while len(visited_nodes) != 0:
                        visited_node = visited_nodes.pop()
                        visited_node.depth = visited_node.find_depth()
                    break
                else:
                    parent = parent.left
                    visited_nodes.append(parent)

    def _compare_nodes(self, n2):
        """
        Compare two nodes. Return False if values of 2 nodes are
        not equal; return True otherwise.
        """
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
            return parent


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

    def breadth_tr(self):
        """
        Return a generator that will return the values in the tree
        using breadth-first traversal, one at a time.
        """
        if self.head:
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
        """
        Return a generator that will return the values in the tree using
        pre-order traversal, one at a time.
        """
        if self.head:
            current_node = self.head
            pending = deque([current_node])
            while len(pending) != 0:
                current_node = pending.pop()
                yield current_node
                if current_node.right is not None:
                    pending.append(current_node.right)
                if current_node.left is not None:
                    pending.append(current_node.left)

    def depth_in_order_tr(self):
        """
        Return a generator that will return the values in the tree using
        in-order traversal, one at a time.
        """
        if self.head:
            current_node = self.head
            visited, yielded = [], []
            while True:
                if current_node.left is not None and \
                        current_node.left not in yielded:
                    visited.append(current_node)
                    current_node = current_node.left
                else:
                    yield current_node
                    yielded.append(current_node)
                    if current_node.right is not None:
                        current_node = current_node.right
                    elif len(visited) != 0:
                        current_node = visited.pop()
                    else:
                        break

    def depth_post_order_tr(self):
        """
        Return a generator that will return the values in the tree using
        post_order traversal, one at a time.
        """
        if self.head:
            current_node = self.head
            visited, yielded = [], []
            while True:
                if current_node.left is not None and \
                        current_node.left not in yielded:
                    visited.append(current_node)
                    current_node = current_node.left
                elif current_node.right is not None and \
                        current_node.right not in yielded:
                    visited.append(current_node)
                    current_node = current_node.right
                else:
                    yield current_node
                    yielded.append(current_node)
                    if len(visited) != 0:
                        current_node = visited.pop()
                    else:
                        break

    def delete(self, value):
        new_node = Node(value)
        node_to_delete = new_node._compare_nodes(self.head)
        if node_to_delete.left or node_to_delete.right:
            #import pdb; pdb.set_trace()
            if node_to_delete.left:
                depth_left = node_to_delete.left.depth
                child1 = node_to_delete.left
            else:
                depth_left = 0
                child1 = None
            if node_to_delete.right:
                depth_right = node_to_delete.right.depth
                child2 = node_to_delete.right
            else:
                depth_right = 0
                child2 = None
            if depth_left >= depth_right:
                current = node_to_delete.left
                while current:
                    parent_of_pending = current.parent
                    pending = current
                    current = current.right
                parent_of_pending.right = None
                parent_of_pending.depth = parent_of_pending.find_depth()
            else:
                current = node_to_delete.right
                while current:
                    parent_of_pending = current.parent
                    pending = current
                    current = current.left
                parent_of_pending.left = None
                parent_of_pending.depth = parent_of_pending.find_depth()
            if child1:
                child1.parent = pending
            if child2:
                child2.parent = pending
            pending.left = child1
            pending.right = child2
            parent_depth = parent_of_pending
            if node_to_delete.parent:
                parent = node_to_delete.parent
                pending.parent = parent
            else:
                pending.parent = None
                self.head = pending
            while parent_depth:
                parent_depth.depth = parent_depth.find_depth()
                parent_depth = parent_depth.parent
        else:
            pending = None
        if node_to_delete.parent:
            parent = node_to_delete.parent
            if parent.left is node_to_delete:
                parent.left = pending
            else:
                parent.right = pending
        else:
            parent = None
            self.head = pending
        parent_depth = parent
        while parent_depth:
            parent_depth.depth = parent_depth.find_depth()
            parent_depth = parent_depth.parent
        node_to_delete.left, node_to_delete.right, node_to_delete.parent = None, None, None
