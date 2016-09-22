#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals


# class Node(object):
#     """Define class for a trie node."""
#     def __init__(self, letter):
#         """Create an instance of Node."""
#         self._dict = {}
#         self.letter = letter
#         self._dict.detdefault(self.letter, {})


class Trie(object):
    """Define class trie."""
    def __init__(self, iterable=None):
        """Create an instance of Trie."""
        self.head = {}

    def insert(self, token):
        token = token + '$'
        current = self.head
        for char in token:
            current.setdefault(char, {})
            current = current[char]
