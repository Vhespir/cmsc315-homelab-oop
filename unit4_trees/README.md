# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
## Implementation

- I implemented a `Node` class that stored a value with left and right child references, and a `BST` class that started with an empty root.
- I implemented recursive `insert`, `search`, and in-order traversal. Smaller values went left, larger values went right, and duplicate track IDs were ignored because IDs are unique.
- I added a `height()` helper to show the most comparisons a search could take.
- I inserted the middle ID (500) first, then the middle of each half, so 7 tracks fit in 3 levels. Every search, found or not, took at most 3 comparisons.
- In-order traversal returned the IDs sorted (`[125, 250, 375, 500, 625, 750, 875]`) without a separate sort, because every left subtree held smaller values and every right subtree held larger ones.
- I searched for two IDs that existed (375, 875) and two that did not (300, 999).
- I tested four edge cases: searching and traversing an empty tree, inserting a duplicate, a single-node tree, and inserting the same IDs in sorted order.

## Real-World Scenario

I modeled a music library lookup. Each track had a numeric track ID, and the BST let the app confirm whether a track was in the library in a few comparisons. The in-order traversal listed the whole library sorted by ID.

## Insertion Order

When I inserted the same 7 IDs in sorted order, each one went to the right of the last, and the tree became a chain 7 levels tall instead of 3. Searching for the largest ID took 7 comparisons instead of 3, the same as a linked list. Track IDs are usually assigned in increasing order as songs are added, so a real system would need a self-balancing tree such as an AVL or red-black tree.
