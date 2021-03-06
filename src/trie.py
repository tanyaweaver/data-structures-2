#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals


class Trie(object):
    """Define class trie."""
    def __init__(self, token=None, iterable=None):
        """
        Create an instance of Trie. <token> must be a string.
        <iterable> must be a list or a tuple of strings.
        """
        self.head = {}
        if token is not None:
            self.insert(token)
        if iterable is not None:
            if not isinstance(iterable, (list, tuple)):
                raise TypeError('the iterable must be a list or a tuple.')
            for token in iterable:
                self.insert(token)

    def insert(self, token):
        """
        Insert the value token into the trie.
        <token> must be a string.
        The token is ignored if already present in the trie.
        """
        if token and isinstance(type(token), type('word')):
            raise TypeError('the token must be a string')
        token = token + '$'
        current = self.head
        for char in token:
            current.setdefault(char, {})
            current = current[char]

    def contains(self, token):
        """Return True if token is int trie. False - if notself."""
        token = token + '$'
        current = self.head
        if current is None:
            return False
        for char in token:
            if char in list(current.keys()):
                current = current[char]
            else:
                return False
        return True
