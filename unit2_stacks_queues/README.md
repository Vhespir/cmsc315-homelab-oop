# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Implementation

- I implemented a Stack using a Python list, with the end of the list as the top. push() and pop() both run in O(1).
- I implemented a Queue using collections.deque, because popleft() removes from the front in O(1). A list would be O(n).
- I handled empty-structure edge cases by returning None from pop(), peek(), dequeue(), and front() instead of letting the program crash.
- I tested single-item structures to confirm they were empty after one removal.
- I modeled a restaurant kitchen: orders waited in a queue (FIFO), and the expo screen's undo history used a stack (LIFO).
- Memory grew linearly, O(n): each added item used one more slot, and removing an item freed it.