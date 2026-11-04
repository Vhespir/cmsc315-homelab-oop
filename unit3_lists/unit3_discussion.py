"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.

SCENARIO:
A fresh food cooler restock list. Items are inserted when they need to be
restocked (urgent items go at the front), removed once they are stocked,
and searched to check whether an item is already on the list.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # list.insert() places the value at the index. Every element already at
    # that index or after it shifts one position to the right.
    # Performance depends on position:
    #   - Inserting at the end shifts nothing: O(1).
    #   - Inserting at the beginning shifts every element: O(n).
    #   - Inserting in the middle shifts about half the elements: O(n).
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate the index first. Without this check, lst.pop() raises an
    # IndexError on a bad index or an empty list and crashes the program.
    # Returning None lets the caller handle the problem safely instead.
    if index < 0 or index >= len(lst):
        return None
    # pop() removes the value and returns it. Every element after it shifts
    # one position left to close the gap, so deleting near the front is O(n)
    # and deleting at the end is O(1).
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search: it checks each element in order, starting at
    # index 0. The list is not sorted, so there is no way to skip ahead.
    # The value could be anywhere. Best case is O(1) (first element), and
    # the worst case is O(n), when the value is last or missing.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    # Every element was checked and none matched
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # 1. Create the restock list for the fresh food cooler
    restock = ["Turkey sandwich", "Fruit cup", "Chicken wrap"]

    # 2. Display the original list
    print(f"Original restock list: {restock}")

    # 3. Insert at the beginning: an urgent item goes first.
    #    Every existing item shifts right (worst case, O(n)).
    insert_at(restock, 0, "Breakfast burrito")
    print(f"After urgent item at the beginning: {restock}")

    # Insert in the middle: about half the items shift right
    insert_at(restock, 2, "Yogurt parfait")
    print(f"After inserting in the middle (index 2): {restock}")

    # Insert at the end: nothing shifts (best case, O(1))
    insert_at(restock, len(restock), "Salad bowl")
    print(f"After inserting at the end: {restock}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete from the beginning: the first item was stocked.
    # Every remaining item shifts left to fill index 0.
    removed = delete_at(restock, 0)
    print(f"Stocked (removed from beginning): {removed}")
    print(f"List now: {restock}")

    # Delete from the middle: items after it shift left
    removed = delete_at(restock, 2)
    print(f"Stocked (removed from middle, index 2): {removed}")
    print(f"List now: {restock}")

    # Delete from the end: no shifting needed
    removed = delete_at(restock, len(restock) - 1)
    print(f"Stocked (removed from end): {removed}")
    print(f"List now: {restock}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # 1. Search for an item that is on the list
    target = "Chicken wrap"
    index = search_value(restock, target)
    print(f"Searching for '{target}': found at index {index}")

    # 2. Search for an item that is not on the list.
    #    Linear search checks every element before returning -1.
    target = "Pizza slice"
    index = search_value(restock, target)
    print(f"Searching for '{target}': returned {index} (not on the list)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: delete using an invalid index.
    # Index 10 does not exist, so delete_at returns None instead of crashing.
    removed = delete_at(restock, 10)
    print(f"Delete at invalid index 10 returned: {removed}")
    print(f"List unchanged: {restock}")

    # Edge case 2: delete using a negative index.
    # Python normally allows negative indexes, but this function rejects them
    # so callers cannot accidentally remove from the end.
    removed = delete_at(restock, -1)
    print(f"Delete at negative index -1 returned: {removed}")

    # Edge case 3: insert into an empty list.
    # Index 0 is the only valid position, and nothing needs to shift.
    empty = []
    insert_at(empty, 0, "Hot dog")
    print(f"Insert into empty list: {empty}")

    # Edge case 4: delete from an empty list.
    # There is nothing to remove, so the function returns None safely.
    empty = []
    removed = delete_at(empty, 0)
    print(f"Delete from empty list returned: {removed}")

    # Edge case 5: search an empty list.
    # The loop never runs, so the function returns -1 immediately.
    print(f"Search empty list returned: {search_value([], 'Fruit cup')}")



if __name__ == "__main__":
    main()