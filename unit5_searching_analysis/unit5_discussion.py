"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.

SCENARIO:
A music library. Tracks are stored by numeric track ID in sorted order,
so the app can use binary search to look one up fast. Linear search is
still used for the "recently added" list, which is kept in the order
songs were added (not sorted), so binary search cannot be used there.
"""


def make_counter():
    """
    Extra helper: a small dict passed into each search so the program
    can count how many comparisons it made. This shows the speed
    difference in actual numbers instead of just Big-O notation.
    """
    return {"comparisons": 0}


def linear_search(lst, target, counter=None):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks items one at a time from index 0. It does not
    # need the list to be sorted, but in the worst case (the target is
    # last or missing) it checks all n items, so it is O(n). Doubling the
    # list size doubles the worst-case work.
    for i in range(len(lst)):
        if counter is not None:
            counter["comparisons"] += 1
        if lst[i] == target:
            # Found: return the position
            return i
    # Every item was checked and none matched
    return -1


def binary_search(lst, target, counter=None):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # low and high mark the part of the list that could still hold the target
    low = 0
    high = len(lst) - 1

    # Loop while the range has at least one item. For an empty list,
    # high is -1, so the loop never runs and the function returns -1.
    while low <= high:
        # Check the middle item of the current range
        mid = (low + high) // 2
        if counter is not None:
            counter["comparisons"] += 1

        if lst[mid] == target:
            # Found the target
            return mid
        elif lst[mid] < target:
            # The target is larger, so everything from low to mid is too
            # small. Discard that half by moving low past mid.
            low = mid + 1
        else:
            # The target is smaller, so everything from mid to high is too
            # large. Discard that half by moving high below mid.
            high = mid - 1
        # Each pass cuts the range about in half, so the number of passes
        # grows with log2(n) instead of n: O(log n).

    # The range is empty, so the target is not in the list
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # 1. A small sorted list of track IDs in the music library
    tracks = [104, 118, 125, 137, 142, 156, 163, 171, 189, 194]
    print(f"Track IDs (sorted): {tracks}")

    # 2-3. Search for a track that exists and one that does not
    for target in [163, 150]:
        lin = make_counter()
        bin_ = make_counter()
        lin_result = linear_search(tracks, target, lin)
        bin_result = binary_search(tracks, target, bin_)
        print(f"Search {target}: linear -> index {lin_result} "
              f"({lin['comparisons']} comparisons), "
              f"binary -> index {bin_result} ({bin_['comparisons']} comparisons)")

    # 4. Both searches return the same answer. 163 is at index 6, so linear
    #    search makes 7 comparisons while binary search makes 4. For 150,
    #    linear search has to check all 10 tracks before returning -1, but
    #    binary search rules it out in 3 because the list is sorted.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # 1. A large sorted library: track IDs 1 through 1,000,000
    library = list(range(1, 1_000_001))
    print(f"Library size: {len(library):,} tracks")

    # 2-3. Search near the start, near the end, and for a missing ID
    for target in [42, 999_999, 1_500_000]:
        lin = make_counter()
        bin_ = make_counter()
        lin_result = linear_search(library, target, lin)
        bin_result = binary_search(library, target, bin_)
        print(f"Search {target:,}: linear {lin['comparisons']:,} comparisons, "
              f"binary {bin_['comparisons']} comparisons "
              f"(both returned {lin_result if lin_result == bin_result else 'DIFFERENT'})")

    # 4. Linear search's cost depends on where the item is. It was fast for
    #    42 because 42 is near the front, but it needed about a million
    #    comparisons for an item near the end or a missing item. Binary
    #    search stayed around 20 comparisons in every case, because
    #    log2(1,000,000) is about 20. Going from 10 tracks to 1,000,000
    #    multiplied linear search's worst case by 100,000, but only added
    #    about 17 comparisons to binary search.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: empty list. Linear search's loop never runs, and binary
    # search's high starts at -1, so both return -1 without an error.
    print(f"Empty list: linear {linear_search([], 104)}, "
          f"binary {binary_search([], 104)}")

    # Edge case 2: single-element list. low and high both start at 0, so
    # binary search checks that one item and either finds it or stops.
    print(f"Single track [137], search 137: binary {binary_search([137], 137)}")
    print(f"Single track [137], search 200: binary {binary_search([137], 200)}")

    # Edge case 3: first and last positions. These are the boundaries
    # where off-by-one mistakes in low/high usually show up.
    print(f"First track (104): binary {binary_search(tracks, 104)}, "
          f"last track (194): binary {binary_search(tracks, 194)}")

    # Edge case 4: unsorted data. The "recently added" list is in the order
    # songs were added, not by ID. Binary search assumes sorted data, so it
    # can discard the half that actually holds the target and miss it.
    # Linear search still works because it checks every item.
    recent = [171, 104, 194, 125, 156]
    print(f"Recently added (unsorted): {recent}")
    print(f"Search 104: linear {linear_search(recent, 104)}, "
          f"binary {binary_search(recent, 104)} (wrong: list is not sorted)")


if __name__ == "__main__":
    main()