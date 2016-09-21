#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from collections import deque


class Node(object):
    """Define class for a node of a binary search tree."""

    def __init__(self, val, left=None, right=None, parent=None):
        """Create an instance of Node."""
        self.value = val
        self._left = left
        self._right = right
        self.depth = 1
        self._parent = parent

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        if node is not None:
            node._parent = self

    @left.deleter
    def left(self):
        self._left = None

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        if node is not None:
            node._parent = self

    @right.deleter
    def right(self):
        self._right = None

    @property
    def parent(self):
        return self._parent

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
        """
        Insert a child for self. Ignore new_node if it's already a child.
         <new_node> must be an instance of Node.
         """
        current = self
        visited_nodes = [self]
        while current:
            if current.value == new_node.value:
                break
            if new_node.value > current.value:
                if current.right is None:
                    current.right = new_node
                    while len(visited_nodes) != 0:
                        visited_node = visited_nodes.pop()
                        visited_node.depth = visited_node.find_depth()
                    return True
                else:
                    current = current.right
                    visited_nodes.append(current)
            elif new_node.value < current.value:
                if current.left is None:
                    current.left = new_node
                    while len(visited_nodes) != 0:
                        visited_node = visited_nodes.pop()
                        visited_node.depth = visited_node.find_depth()
                    return True
                else:
                    current = current.left
                    visited_nodes.append(current)
        return False

    def _find_next_bigger(self):
        """Find next bigger node among childer of self."""
        current = self.right
        if current:
            while current.left:
                current = current.left
        return current

    def _find_previous_smaller(self):
        """Find previous smaller node among children of self."""
        current = self.left
        if current:
            while current.right:
                current = current.right
        return current

    def _delete_leaf(self):
        """Delete a node that doesn't have children."""
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            parent = self.parent
            while parent:
                parent.depth = parent.find_depth()
                parent = parent.parent

    def _balance(self):
        """
        Return negative integer if the depth of the right child of the
        node is bigger than the depth of the left child. Return positive
        integer if the depth of the left child of the node is bigger than
        the depth of the right child. Return 0 if depth of the left
        and right child are the same.
        """
        depth_left, depth_right = 0, 0
        if self.left:
            depth_left = self.left.find_depth()
        if self.right:
            depth_right = self.right.find_depth()
        return depth_left - depth_right

    # def left_rotation(self):
    #     grandparent = self.parent.parent
    #     if grandparent._balance() == -2:
    #         if grandparent.parent:
    #             grandparent.parent.right = self.parent
    #         self.parent.left = grandparent
    #         grandparent.right = None


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

    def return_node(self, value):
        """
        Return Node(val) from the tree or
        False if Node is not in the tree.
        """
        current = self.head
        while current:
            if value == current.value:
                return current
            else:
                if value > current.value:
                    current = current.right
                else:
                    current = current.left
        return False

    def insert(self, value):
        """
        Insert the value into bst. If value is already present,
        it will be ignored.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.counter += 1
        else:
            if self.head._insert_node(new_node):
                self.counter += 1

    def contains(self, value):
        """
        Returns True if the value in the bst, False if not.
        """
        result = self.return_node(value)
        if result:
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

    def breadth_first(self):
        """
        Return a generator that will return the values in the tree
        using breadth-first traversal, one at a time.
        """
        if self.head:
            current_node = self.head
            pending = deque([current_node])
            while len(pending) != 0:
                current_node = pending.pop()
                yield current_node.value
                if current_node.left is not None:
                    pending.appendleft(current_node.left)
                if current_node.right is not None:
                    pending.appendleft(current_node.right)

    def pre_order(self):
        """
        Return a generator that will return the values in the tree using
        pre-order traversal, one at a time.
        """
        if self.head:
            current_node = self.head
            pending = deque([current_node])
            while len(pending) != 0:
                current_node = pending.pop()
                yield current_node.value
                if current_node.right is not None:
                    pending.append(current_node.right)
                if current_node.left is not None:
                    pending.append(current_node.left)

    def in_order(self):
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
                    yield current_node.value
                    yielded.append(current_node)
                    if current_node.right is not None:
                        current_node = current_node.right
                    elif len(visited) != 0:
                        current_node = visited.pop()
                    else:
                        break

    def post_order(self):
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
                    yield current_node.value
                    yielded.append(current_node)
                    if len(visited) != 0:
                        current_node = visited.pop()
                    else:
                        break

    def delete(self, value):
        """Delete a node from the tree."""
        node_to_delete = self.return_node(value)
        if node_to_delete:
            child_left, child_right = node_to_delete.left, node_to_delete.right
            depth_left, depth_right = 0, 0
            if child_left:
                depth_left = child_left.find_depth()
            if child_right:
                depth_right = child_right.find_depth()
            if depth_left == 0 and depth_right == 0:
                if not node_to_delete.parent:
                    self.head = None
                node_to_delete._delete_leaf()
                self.counter -= 1
            else:
                if depth_left >= depth_right:
                    replacement = node_to_delete._find_previous_smaller()
                else:
                    replacement = node_to_delete._find_next_bigger()
                replacement._delete_leaf()
                node_to_delete.value = replacement.value
                self.counter -= 1

    def left_rotation(self, node1, node2):
        if node2.parent:
            node2.parent.right = node1
        else:
            self.head = node1
        node2.right = None
        node1.left = node2
        node2.find_depth()
        current = node1
        while current:
            current.find_depth()
            current = current.parent
