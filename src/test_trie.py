#!/usr/bin/env python
# -*- coding: utf -8 -*-

from trie import Trie
import pytest

TOKEN = [
    (['c'], 'c'),
    (['cat'], 'c'),
    (['c', 'ca', 'cat', 'cats', 'catss'], 'c'),
    (['cat', 'code', 'codes', 'clap', 'clown'], 'c'),
    (['ca¡', 'ce¥abc', 'cs§'], 'c')
]


@pytest.mark.parametrize('iterable, start', TOKEN)
def test_depth_first1(iterable, start):
    """Prove that depth_first() generates expected tokens."""
    iterable = iterable
    trie = Trie(iterable=iterable)
    result = []
    for token in trie.depth_first(start):
        result.append(token)
    for word in iterable:
        assert word in result


def test_depth_first2():
    """Prove that depth_first() generates None if the trie is empty."""
    trie = Trie()
    result = []
    for token in trie.depth_first('a'):
        result.append(token)
    assert result == []


def test_depth_first3():
    """
    Prove that depth_first() returns None if start is not
    a key in the trie.head dictionary.
    """
    trie = Trie(iterable=['dome', 'bag', 'ice', 'bolt'])
    result = []
    for token in trie.depth_first('m'):
        result.append(token)
    assert result == []


def test_depth_first4():
    """Prove that depth_first() generates expected tokens."""
    trie = Trie(iterable=['dome', 'bag', 'ice', 'bolt'])
    result = []
    for token in trie.depth_first('b'):
        result.append(token)
    for x in ['bag', 'bolt']:
        assert x in result


def test_depth_first5():
    """
    Prove that depth_first() doesn't generate extra tokens
    compared to what is expected.
    """
    trie = Trie(iterable=['dome', 'bag', 'ice', 'bolt'])
    result = []
    for token in trie.depth_first('b'):
        result.append(token)
    assert len(result) == 2


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


def test_contains_False1():
    """
    Prove that contains() returns False if looking in an empty trie.
    """
    trie = Trie()
    assert trie.contains('ma') is False


def test_contains_False2():
    """
    Prove that contains() returns False if token is not in the trie.
    """
    trie = Trie(iterable=['man', 'mantle'])
    assert trie.contains('ma') is False


def test_contains_False3():
    """
    Prove that contains() returns False if token is not in the trie.
    """
    trie = Trie(iterable=['man', 'mantle'])
    assert trie.contains('mant') is False


def test_contains_False4():
    """
    Prove that contains() returns False if token is not in the trie.
    """
    trie = Trie(iterable=['man', 'mantle'])
    assert trie.contains('mantles') is False


def test_contains_True1():
    """
    Prove that contains() returns True if token is in the trie.
    """
    trie = Trie(iterable=['man', 'mantle'])
    assert trie.contains('man') is True


def test_contains_True2():
    """
    Prove that contains() returns True if token is in the trie.
    """
    trie = Trie(iterable=['man', 'mantle'])
    assert trie.contains('mantle') is True


def test_insert_type_error():
    """
    Prove that a Type error is raised when trying to
    insert a token that is not a str.
    """
    with pytest.raises(TypeError):
        trie = Trie()
        trie.insert(25637)


def test_insert_value_error():
    """
    Prove that a value error is raised when trying to insert a token
    that contains '$' character.
    """
    with pytest.raises(ValueError):
        trie = Trie()
        trie.insert('abc$abc')


def test_iterable_type():
    """
    Prove that a Type error is raised when trying to create a trie
    with an iterable that is not a list or a tuple.
    """
    with pytest.raises(TypeError):
        trie = Trie(iterable=1341345)
