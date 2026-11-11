"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.

SCENARIO:
A music library lookup. Each track has a numeric track ID. The BST
stores the IDs so the app can quickly check whether a track is in the
library, and an in-order traversal lists the whole library sorted by ID.
"""

# Track titles for the IDs used in this demo. The BST stores only the
# IDs (the keys); this dictionary looks up the title for display.
TRACK_TITLES = {
    500: "Clair de Lune",
    250: "Moonlight Sonata",
    750: "Canon in D",
    125: "Fur Elise",
    375: "Gymnopedie No. 1",
    625: "The Four Seasons: Spring",
    875: "The Blue Danube",
}


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        # A new node starts as a leaf: it holds a value and has no children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        # An empty tree has no root. Every operation checks for this.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Insertion must follow the BST rule (smaller left, larger right)
        # so that every later search knows which side to check. If a value
        # were placed on the wrong side, search would never find it.
        # The helper returns the (possibly new) root, so an empty tree
        # gets its first node here.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: an empty spot was found, so the new node goes here
        if node is None:
            return Node(value)

        if value < node.value:
            # Smaller values belong in the left subtree
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger values belong in the right subtree
            node.right = self._insert_recursive(node.right, value)
        # If value == node.value, it is a duplicate. Track IDs are unique,
        # so the duplicate is ignored and the tree is left unchanged.

        # Return this node so the parent's left/right link stays connected
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # A linear search may check every item. A BST search compares the
        # target to one node and then skips the entire other subtree, so
        # each step removes about half of the remaining items. In a
        # balanced tree that takes about log2(n) steps instead of n.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case: reached an empty spot, so the value is not in the tree
        if node is None:
            return False
        # Base case: found the value
        if value == node.value:
            return True
        # Smaller: it can only be in the left subtree
        if value < node.value:
            return self._search_recursive(node.left, value)
        # Larger: it can only be in the right subtree
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Start with an empty list; the helper fills it as it visits nodes.
        # An empty tree simply returns [].
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Base case: nothing to visit
        if node is None:
            return
        # Everything in the left subtree is smaller than this node,
        # so it is visited first.
        self._inorder_recursive(node.left, values)
        # Then this node, which is larger than everything to its left
        values.append(node.value)
        # Everything in the right subtree is larger, so it comes last.
        # Applying this at every node produces ascending (sorted) order.
        self._inorder_recursive(node.right, values)

    def height(self):
        """
        Extra helper: returns the number of levels in the tree.
        This is the most comparisons a search can take, so it shows
        how insertion order affects performance.
        """
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        # An empty subtree adds no levels
        if node is None:
            return 0
        # One level for this node plus the taller of its two subtrees
        return 1 + max(self._height_recursive(node.left),
                       self._height_recursive(node.right))


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # 1. Create the music library tree
    library = BST()

    # 2-3. Insert 7 IDs. The middle ID (500) goes first so it becomes
    #      the root, then the middle of each half, which keeps the tree
    #      balanced: 3 levels for 7 tracks.
    ids = [500, 250, 750, 125, 375, 625, 875]
    for track_id in ids:
        library.insert(track_id)
        # 4. Display each value as it is inserted, and which side it went to
        if track_id == 500:
            place = "root"
        elif track_id < 500:
            place = "left subtree (smaller than 500)"
        else:
            place = "right subtree (larger than 500)"
        print(f"Inserted {track_id} ({TRACK_TITLES[track_id]}) -> {place}")

    # 5. Each comparison in this tree rules out a whole subtree. With 7 tracks
    #    in 3 levels, any search takes at most 3 comparisons instead of 7.
    print(f"Tree height: {library.height()} levels for {len(ids)} tracks")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # 1. In-order visits left subtree, node, right subtree
    sorted_ids = library.inorder()

    # 2. The IDs come out sorted even though they were inserted out of order
    print(f"Track IDs in order: {sorted_ids}")
    print("Library sorted by track ID:")
    for track_id in sorted_ids:
        print(f"  {track_id}: {TRACK_TITLES[track_id]}")

    # 3. This is sorted because every left subtree holds smaller IDs and
    #    every right subtree holds larger ones, so left-node-right always
    #    visits smaller IDs first. No separate sort was needed.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # 1. IDs that exist: 375 goes 500 -> left to 250 -> right to 375.
    #    875 goes 500 -> right to 750 -> right to 875.
    for track_id in [375, 875]:
        print(f"Search {track_id}: {library.search(track_id)} ({TRACK_TITLES[track_id]})")

    # 2. IDs that do not exist: the search reaches an empty child and
    #    stops. 300 goes 500 -> 250 -> 375 -> empty left child.
    #    999 goes 500 -> 750 -> 875 -> empty right child.
    for track_id in [300, 999]:
        print(f"Search {track_id}: {library.search(track_id)} (not in the library)")

    # 3. Every search, found or not, took at most 3 comparisons.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case 1: empty tree. The root is None, so search hits the base
    # case right away and returns False, and traversal returns [].
    empty = BST()
    print(f"Search empty tree for 500: {empty.search(500)}")
    print(f"Traverse empty tree: {empty.inorder()}")

    # Edge case 2: duplicate insert. 500 is already the root, so the
    # duplicate is ignored and the track count stays at 7.
    library.insert(500)
    print(f"After inserting duplicate 500: {len(library.inorder())} tracks")

    # Edge case 3: single-node tree. The root is also a leaf.
    single = BST()
    single.insert(125)
    print(f"Single-node tree: {single.inorder()}, height {single.height()}")

    # Edge case 4: insertion order. The same 7 IDs inserted in sorted
    # order each go to the right of the last one, so the tree becomes a
    # chain like a linked list. Searching for 875 now takes 7 comparisons.
    chain = BST()
    for track_id in sorted(ids):
        chain.insert(track_id)
    print(f"Same IDs inserted in sorted order: height {chain.height()} "
          f"(balanced tree was {library.height()})")


if __name__ == "__main__":
    main()
