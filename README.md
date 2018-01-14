# String Reverse in Python
In this assignment, you'll design and implement one of the string manipulation functions that is commonly asked during interviews.
Remember that a string is an array of characters. Algorithms that worked on restricted arrays will work on strings as well.

## Exercise
Design and implement a method to reverse a string. For example, if the method is called with an input parameter of "Lovelace", the method should return a new string object with the value "ecalevoL". Share and explain the time and space complexities for your solution.

## Python Considerations
The Ruby version of this assignment involved reversing a string in place. Unlike Ruby strings, Python strings are immutable, which means they can't be changed after they are initialized. Because strings cannot be modified in place, a new string must be created whenever a change must be made to a string.

**Note**: Do not use Python provided functionality for `reversed()`, `reverse()`, or string slicing (`"string"[::-1]`). You may use `len()`.

## Running the Tests
Install `pytest`
```terminal
pip install pytest
```
To run all tests, navigate to the same directory as the test file and run:
```terminal
pytest test_string_reverse.py
```
Alternatively, to exit instantly on first error or failed test, run:
```terminal
pytest -x test_string_reverse.py
```

See [pytest documentation](http://pytest.org/latest/) for more information about `pytest`.
