# Assignment for Code 401- Python: Data-structures implementation
[![Travis](https://travis-ci.org/tanyaweaver/data-structures-2.svg?branch=traversals)](https://travis-ci.org/tanyaweaver/data-structures-2.svg?branch=traversals)
## This module contains implementations of
## 1. Binary Search Tree
###Methods
* insert(self, val) -    insert the value into bst. If value is already present, it will be ignored.
* contains(self, val) - Returns True if the value in the bst, False if not.
* size(self) - Return the integer size of the bst. Return zero if the bst is empty.
* depth(self) - Return an integer representing the total levels in a tree.
* balance(self) - Return an integer that represents how well balanced the tree is:
                    - a positive value if the tree is higher on the left than the right;
                    - a negative value if the tree is higher on the right than the left;
                    - zero if the tree is ideally-balanced.
* delete(self, val) - Remove val from the tree if present, if not present this method is a    no-op. Return None in all cases.

###Traversal methods
* in_order(self) - Return a generator that will return the values in the tree using in-order traversal, one at a time.
* pre_order(self) - Return a generator that will return the values in the tree using pre-order traversal, one at a time.
* post_order(self) - Return a generator that will return the values in the tree using post_order traversal, one at a time.
* breadth_first(self) - Return a generator that will return the values in the tree using breadth-first traversal, one at a time.


## 2. Trie
###Methods
* insert(self, token) -    Insert the value token into the trie. If token is already present, it will be ignored.
* contains(self, token) - Returns True if token is present in the trie, False if not.

## 3. Sorting Algorithms
* Radix sort - A non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits 
which share the same significant position and value. (source: https://en.wikipedia.org/wiki/Radix_sort)


# Instructions
## Usage
Clone the repo and install modules:
```
pip install -e ./
```

To use binary search tree
```python
from bst import Bst
my_bst = Bst([1, 2, 3])
```

To use trie
```python
from trie import Trie
my_trie = Trie(token='tokentoinsert', iterable=['cat', 'dog'])
```
To use Radix Sort
```
$python src/radixsort.py
radixsort([7, 1, 35, 6]) # => [1, 6, 7, 35]
```