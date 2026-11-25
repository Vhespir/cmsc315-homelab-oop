"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def show(library, label):
    """Prints the library one track per line."""
    print(f"{label} ({len(library)} tracks):")
    if not library:
        print("  (empty)")
    for track_id, title in library.items():
        print(f"  {track_id}: {title}")


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")

    # Music library: track ID is the key, song title is the value
    library = {}

    # Each key is hashed to pick a slot, so inserts are O(1) on average
    library[104] = "Midnight City"
    library[118] = "Teardrop"
    library[125] = "Breathe"
    library[137] = "Nightcall"
    library[142] = "Resonance"
    library[156] = "Genesis"

    show(library, "Library")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # The key is hashed again to go straight to its slot, no searching
    for track_id in [137, 104]:
        print(f"Lookup {track_id}: {library[track_id]}")

    print(f"Is track 142 in the library? {142 in library}")
    print(f"Is track 999 in the library? {999 in library}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")

    show(library, "Before update")

    # Same key, so only the value is replaced and no duplicate is made
    library[125] = "Breathe (Remastered)"

    show(library, "After update")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")

    show(library, "Before delete")

    # The key is hashed to find its slot, then the pair is removed
    del library[156]
    removed = library.pop(118)
    print(f"Removed 156 with del and 118 with pop() ({removed})")

    show(library, "After delete")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")

    # Missing key: [] raises KeyError, get() returns a default
    try:
        print(library[999])
    except KeyError:
        print("library[999] raised KeyError")
    print(f"library.get(999, 'Track not found') -> {library.get(999, 'Track not found')}")

    # Deleting a missing key safely with a default
    print(f"library.pop(999, None) -> {library.pop(999, None)}")

    # Updating a missing key just adds it
    library[168] = "Strobe"
    print(f"library[168] = 'Strobe' added a new track, size is now {len(library)}")

    # Empty dictionary
    empty = {}
    print(f"Empty dict: get(104) -> {empty.get(104)}, len -> {len(empty)}")

    # Lists can change, so they can't be keys
    try:
        library[[200, 201]] = "Playlist"
    except TypeError:
        print("Using a list as a key raised TypeError")

    print("\n=== COLLISIONS (8 buckets) ===")

    # 104 and 168 both land in bucket 0 (104 % 8 and 168 % 8 are both 0)
    buckets = [[], [], [], [], [], [], [], []]
    for track_id in library:
        buckets[track_id % 8].append(track_id)

    for i in range(8):
        print(f"  bucket {i}: {buckets[i]}")

    print("\n=== PLAY COUNTS ===")

    play_log = [104, 137, 104, 168, 137, 104, 142, 999]
    play_counts = {}
    for track_id in play_log:
        if track_id not in library:
            print(f"  Skipped unknown track {track_id}")
            continue
        play_counts[track_id] = play_counts.get(track_id, 0) + 1

    for track_id, count in play_counts.items():
        print(f"  {library[track_id]}: {count}")


if __name__ == "__main__":
    main()
