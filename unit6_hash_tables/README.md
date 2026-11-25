# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
## Implementation

- I used a dictionary as the hash table for my music library. The track ID was the key and the song title was the value.
- I inserted 6 tracks. Each key was hashed to pick a slot, so inserts and lookups were O(1) on average.
- I looked up tracks 137 and 104 by key and used `in` to check whether a track existed.
- I updated track 125 to "Breathe (Remastered)". The key already existed, so only the value changed.
- I deleted track 156 with `del` and track 118 with `pop()`, which also returned the removed title.
- I added a `show()` helper to print the library before and after each change.

## Edge Cases

- **Missing key:** `library[999]` raised `KeyError`, but `get()` returned a default instead.
- **Deleting a missing key:** `pop(999, None)` returned `None` without an error.
- **Updating a missing key:** assigning `library[168]` did not fail. It added a new track.
- **Empty dictionary:** `get()` and `len()` still worked.
- **List as a key:** raised `TypeError`, because a list can change and its hash would change with it.

## Collisions

I made an 8-bucket table to show a collision. Tracks 104 and 168 both landed in bucket 0, so finding 168 meant checking 104 first. If too many keys land in the same bucket, lookups slow down from O(1) toward O(n). Python's dictionary avoids this by resizing before the table gets too full.

## Real-World Scenario

I added play counts. Each time a song played, its count went up by one with `get(track_id, 0) + 1`. A play for track 999 was skipped because that track was not in the library.
