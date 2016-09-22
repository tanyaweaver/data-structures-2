#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
from trie import Trie


def test_trie_init():
    """
    Prove that head of a new instance of trie is an empty dict.
    """
    trie = Trie()
    assert trie.head == {}


def test_insert1():
    """
    Prove that the head is a nested dict,
    with '$' as the key in the most inner dict.
    """
    trie = Trie()
    trie.insert('a')
    assert trie.head == {'a': {'$': {}}}


def test_insert3():
    """
    Prove that the head is a nested dict,
    with '$' as the key in the most inner dict.
    """
    trie = Trie()
    trie.insert('cat')
    assert trie.head == {'c': {'a': {'t': {'$': {}}}}}


def test_insert4():
    """
    Prove that the token is ignored when it is already in the trie.
    """
    trie = Trie()
    trie.insert('cat')
    trie.insert('cat')
    assert trie.head == {'c': {'a': {'t': {'$': {}}}}}


def test_insert5():
    """
    Prove that the head is a nested dict of the expected stracture.
    """
    trie = Trie()
    trie.insert('cat')
    trie.insert('car')
    assert trie.head == {
        'c': {
            'a': {
                't': {'$': {}},
                'r': {'$': {}}
                }
            }
        }


def test_insert6():
    """
    Prove that the head is a nested dict of the expected stracture.
    """
    trie = Trie()
    trie.insert('cat')
    trie.insert('bar')
    assert trie.head == {
        'c': {
            'a': {
                't': {
                    '$': {}
                      }
                }
            },
        'b': {
            'a': {
                'r': {
                    '$': {}
                }
            }
        }
    }


def test_insert7():
    """
    Prove that the head is a nested dict of the expected stracture.
    """
    trie = Trie()
    trie.insert('man')
    trie.insert('mantle')
    assert trie.head == {
        'm': {
            'a': {
                'n': {
                    '$': {},
                    't': {'l': {'e': {'$': {}}}}
                }
            }
        }
    }
