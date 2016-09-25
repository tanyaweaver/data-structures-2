# Assignment for Code 401- Python: Data-structures implementation
[![Travis](https://travis-ci.org/tanyaweaver/data-structures-2.svg?branch=traversals)](https://travis-ci.org/tanyaweaver/data-structures-2.svg?branch=traversals)
## This module contains implementations of Binary Search Tree
An instance of a tree can be created with an iterable and by default, the tree will balance itself after inserting each item from the iterable. To avoid the self-balancing step, Set
self_balance to None.

###Methods
* insert(val) -    insert the value into bst. If value is already present, it will be ignored.
  By default, the tree performs self-balancing after the insertion. Set self_balance to False to avoid self-balancing.
* contains(val) - Returns True if the value in the bst, False if not.
* size(self) - Return the integer size of the bst. Return zero if the bst is empty.
* depth(self) - Return an integer representing the total levels in a tree.
* balance(self) - Return an integer that represents how well balanced the tree is:
                    - a positive value if the tree is higher on the left than the right;
                    - a negative value if the tree is higher on the right than the left;
                    - zero if the tree is ideally-balanced.
* delete(self, val) - Remove val from the tree if present, if not present this method is
  a no-op. Return None in all cases. By default, the tree performs self-balancing after the deletion. Set self_balance to False to avoid self-balancing.


###Traversal methods
* in_order(self) - Return a generator that will return the values in the tree using in-order traversal, one at a time.
* pre_order(self) - Return a generator that will return the values in the tree using pre-order traversal, one at a time.
* post_order(self) - Return a generator that will return the values in the tree using post_order traversal, one at a time.
* breadth_first(self) - Return a generator that will return the values in the tree using breadth-first traversal, one at a time.

# Instructions
## Usage
To install module
```
pip install .
```

To use binary search tree
```python
from bst import Bst
my_bst = Bst(iterable=[1, 2, 3], self_balance=True)
```
To avoid self-balancing, set self_balance to False:
```python
my_bst = Bst(iterable=[1, 2, 3], self_balance=False) 
```
