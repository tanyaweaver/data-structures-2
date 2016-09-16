# Assignment for Code 401- Python: Data-structures implementation 
[![Travis](https://travis-ci.org/tanyaweaver/data-structures-2/jobs/160330817#)](https://travis-ci.org/tanyaweaver/data-structures-2/jobs/160330817#)
## This module contains implementations of Binary Search Tree
###Methods
* insert(val) -    insert the value into bst. If value is already present, it will be ignored.
* contains(val) - Returns True if the value in the bst, False if not.
* size(self) - Return the integer size of the bst. Return zero if the bst is empty.
* depth(self) - Return an integer representing the total levels in a tree.
* balance(self) - Return an integer that represents how well balanced the tree is:
                    - a positive value if the tree is higher on the left than the right;
                    - a negative value if the tree is higher on the right than the left;
                    - zero if the tree is ideally-balanced.

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
my_bst = Bst([1, 2, 3])
```

