# Assignment for Code 401- Python: Data-structures implementation 
## This module contains implementations of Binary Search Tree, including methods:
* insert(val) -    insert the value into bst. If value is already present, it will be ignored.
* contains(val) - Returns True if the value in the bst, False if not.
* size() - Return the integer size of the bst. Return zero if the bst is empty.
* depth() - Return an integer representing the total levels in a tree.
* balance() - Return an integer that represents how well balanced the tree is:
                    - a positive value if the tree is higher on the left than the right;
                    - a negative value if the tree is higher on the right than the left;
                    - zero if the tree is ideally-balanced.

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

