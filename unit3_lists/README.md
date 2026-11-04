# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Implementation

- I implemented `insert_at()` with `list.insert()`. Inserting at the end shifted nothing (O(1)), while inserting at the beginning shifted every element right (O(n)).
- I implemented `delete_at()` with `list.pop()`. I validated the index first and returned `None` for invalid or negative indexes, so a bad index could not crash the program or accidentally remove from the end.
- I implemented `search_value()` as a linear search that checked each element in order and returned its index, or `-1` if the value was missing. The list was unsorted, so a sequential scan was the only option (O(n)).
- I tested insertion and deletion at the beginning, middle, and end, and searched for both an existing and a missing value.
- I tested five edge cases: an out-of-range index, a negative index, inserting into an empty list, deleting from an empty list, and searching an empty list.

## Real-World Scenario

I modeled a fresh food cooler restock list. Urgent items were inserted at the front, items were removed once they were stocked, and the list was searched to check whether an item was already on it. A Python list fit this scenario because the list stayed small and items were often read by position, but inserting urgent items at the front showed the O(n) cost of shifting every element. If the list were large and front insertions were frequent, a linked list would perform better there, since inserting at the head only updates a pointer.
