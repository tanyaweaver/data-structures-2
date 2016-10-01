# #!/usr/bin/env python
# # -*- coding: utf -8 -*-

# from __future__ import unicode_literals
# from trie import Trie
# import pytest


# def test_trie_init():
#     """
#     Prove that head of a new instance of trie is an empty dict.
#     """
#     trie = Trie()
#     assert trie.head == {}


# def test_insert1():
#     """
#     Prove that the head is a nested dict,
#     with '$' as the key in the most inner dict.
#     """
#     trie = Trie()
#     trie.insert('a')
#     assert trie.head == {'a': {'$': {}}}


# def test_insert3():
#     """
#     Prove that the head is a nested dict,
#     with '$' as the key in the most inner dict.
#     """
#     trie = Trie()
#     trie.insert('cat')
#     assert trie.head == {'c': {'a': {'t': {'$': {}}}}}


# def test_insert4():
#     """
#     Prove that the token is ignored when it is already in the trie.
#     """
#     trie = Trie()
#     trie.insert('cat')
#     trie.insert('cat')
#     assert trie.head == {'c': {'a': {'t': {'$': {}}}}}


# def test_insert5():
#     """
#     Prove that the head is a nested dict of the expected stracture.
#     """
#     trie = Trie()
#     trie.insert('cat')
#     trie.insert('car')
#     assert trie.head == {
#         'c': {
#             'a': {
#                 't': {'$': {}},
#                 'r': {'$': {}}
#                 }
#             }
#         }


# def test_insert6():
#     """
#     Prove that the head is a nested dict of the expected stracture.
#     """
#     trie = Trie()
#     trie.insert('cat')
#     trie.insert('bar')
#     assert trie.head == {
#         'c': {
#             'a': {
#                 't': {
#                     '$': {}
#                       }
#                 }
#             },
#         'b': {
#             'a': {
#                 'r': {
#                     '$': {}
#                 }
#             }
#         }
#     }


# def test_insert7():
#     """
#     Prove that the head is a nested dict of the expected stracture.
#     """
#     trie = Trie()
#     trie.insert('man')
#     trie.insert('mantle')
#     assert trie.head == {
#         'm': {
#             'a': {
#                 'n': {
#                     '$': {},
#                     't': {'l': {'e': {'$': {}}}}
#                 }
#             }
#         }
#     }


# def test_contains_False1():
#     """
#     Prove that contains() returns False if looking in an empty trie.
#     """
#     trie = Trie()
#     assert trie.contains('ma') is False


# def test_contains_False2():
#     """
#     Prove that contains() returns False if token is not in the trie.
#     """
#     trie = Trie(iterable=['man', 'mantle'])
#     assert trie.contains('ma') is False


# def test_contains_False3():
#     """
#     Prove that contains() returns False if token is not in the trie.
#     """
#     trie = Trie(iterable=['man', 'mantle'])
#     assert trie.contains('mant') is False


# def test_contains_False4():
#     """
#     Prove that contains() returns False if token is not in the trie.
#     """
#     trie = Trie(iterable=['man', 'mantle'])
#     assert trie.contains('mantles') is False


# def test_contains_True1():
#     """
#     Prove that contains() returns True if token is in the trie.
#     """
#     trie = Trie(iterable=['man', 'mantle'])
#     assert trie.contains('man') is True


# def test_contains_True2():
#     """
#     Prove that contains() returns True if token is in the trie.
#     """
#     trie = Trie(iterable=['man', 'mantle'])
#     assert trie.contains('mantle') is True


# def test_token_type():
#     """
#     Prove that a Type error is raised if token is not a str.
#     """
#     with pytest.raises(TypeError):
#         trie = Trie(25637)


# def test_iterable_type():
#     """
#     Prove that a Type error is raised if iterable is not a list
#     or a tuple.
#     """
#     with pytest.raises(TypeError):
#         trie = Trie(iterable=1341345)
