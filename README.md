# Python Learning

This repository contains Python code and exercises for learning basic Python concepts. The following files explore data types, string manipulations, list manipulations, and more.

## Project Structure

```bash
pythonLearning/
│
├── Day1/
│   ├── DataTypes.py
│   ├── String.py
│   ├── List.py
│   ├── Tuples.py
│   └── Sets.py
├── .gitignore
└── README.md

```
### Files:

- **`DataTypes.py`**: Contains examples of various Python data types, such as variables, lists, tuples, ranges, dictionaries, sets, and frozensets. This file demonstrates how to work with and manipulate these data structures.

  *Key Topics*:
  - Variable declaration and type checking
  - List manipulation
  - Tuple immutability
  - Ranges converted to lists and tuples
  - Dictionary operations (adding, updating values)
  - Set operations and properties (removing duplicates)
  - Frozenset immutability

- **`String.py`**: Includes string manipulation examples in Python, such as checking for substrings, accessing string characters, checking if a string contains certain values, and measuring string length.

  *Key Topics*:
  - String indexing
  - Checking if a substring exists in a string
  - String length measurement

- **`List.py`**: Demonstrates operations and properties of Python lists, including creating lists, accessing elements, modifying values, handling heterogeneous data, and list operations such as appending, inserting, and popping elements.

  *Key Topics*:
  - List creation and element access
  - Modifying list elements
  - Handling heterogeneous data types in a list
  - Dynamic resizing of lists (append, insert)
  - Nested list access and manipulation (popping elements)
  - Looping through lists (element and index)
  - Case-insensitive sorting
  - Reversing lists
  - Copying lists (using copy() and list() methods)
    
- **`Tuples.py`**: Illustrates various operations with tuples, including creating tuples, accessing elements, updating tuples by converting them to lists, adding and removing items, unpacking tuples, and looping through them.

  *Key Topics*:
  - Tuple creation and length
  - Creating a tuple with one item
  - Using the tuple() constructor
  - Accessing tuple elements
  - Updating tuples (converting to list and back)
  - Adding and removing items from tuples
  - Unpacking tuples
  - Looping through tuples and using asterisk * for unpacking
    
- **`Sets.py`**: Explores various operations with sets in Python, including set creation, handling mixed data types, adding elements, removing elements, and joining sets. It covers advanced set operations such as union, difference, and symmetric difference.

  *Key Topics*:
  - **Set creation**: Creating sets with literals and the `set()` constructor.
  - **Handling duplicates**: Understanding how `True/1` and `False/0` are treated as duplicates.
  - **Accessing elements**: Iterating through set elements using loops.
  - **Adding items**: Using `add()` to add items and `update()` to add multiple elements or iterable items like lists.
  - **Removing items**: Using `remove()` and `discard()`, and understanding how `pop()` removes a random element.
  - **Clearing and deleting sets**: Using `clear()` to empty a set and `del` to delete a set.
  - **Joining sets**: Using `union()`, `|`, and `update()` to combine sets.
  - **Difference and symmetric difference**:
    - `difference()` and `-`: Return a new set with elements present in the first set but not in the second.
    - `difference_update()`: Modifies the original set to keep only unique elements.
    - `symmetric_difference()` and `^`: Return a new set with elements not present in both sets.
    - `symmetric_difference_update()`: Modifies the original set to only keep unique elements from both sets.


