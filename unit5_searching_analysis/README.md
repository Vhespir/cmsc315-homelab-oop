# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.
## Implementation

- I implemented `linear_search()`, which checked each item from index 0 and returned its index, or -1 if the target was missing. It did not need sorted data, but its worst case was O(n).
- I implemented `binary_search()` with `low` and `high` markers. It checked the middle item and discarded the half that could not hold the target, so each pass cut the search space about in half: O(log n).
- I added an optional comparison counter so the program printed how many comparisons each search made.

## Results

- **Small dataset (10 tracks):** finding track 163 took 7 comparisons with linear search and 4 with binary search. A missing ID took 10 linear comparisons and 3 binary comparisons.
- **Large dataset (1,000,000 tracks):** binary search stayed at about 20 comparisons in every test. Linear search took 42 comparisons for an ID near the front but about 1,000,000 for an ID near the end or a missing ID.
- Going from 10 to 1,000,000 tracks multiplied linear search's worst case by 100,000 but only added about 17 comparisons to binary search.

## Edge Cases

- **Empty list:** both searches returned -1 without an error.
- **Single-element list:** binary search found the one track, or returned -1 for a missing one.
- **First and last positions:** binary search found both boundary tracks correctly.
- **Unsorted list:** binary search returned the wrong answer (-1) on the unsorted "recently added" list, even though the track was there. Linear search still found it.

## Real-World Scenario

I modeled a music library. The main library was sorted by track ID, so binary search could look up any track in about 20 comparisons. The "recently added" list stayed in the order songs were added, so only linear search could be used on it. That list was also small, so a linear scan was fast enough and there was no reason to sort it.
