"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.

SCENARIO:
A restaurant kitchen. Incoming food orders wait in a Queue so they
are cooked in the order they arrived (FIFO). The expo screen keeps a
Stack of recent screen actions so the most recent one can be undone
first (LIFO).
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # The end of the list is treated as the top of the stack.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # append() places the new value on top (end of the list), so it will
        # be the first one removed. That is what makes the stack LIFO.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # An empty stack has nothing to remove. Instead of letting Python
        # raise an IndexError and crash, return None so the caller can check.
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek() reads the top value (last item) but leaves the stack unchanged.
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # deque removes from the front in O(1) time. A list would be O(n),
        # because every remaining item would shift left.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values join at the back, so older values stay ahead of them
        # and leave first. That is what makes the queue FIFO.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # An empty deque would raise IndexError on popleft(), so return None
        # instead and let the caller decide what to do.
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # front() returns the oldest value (next to be served) without removing it.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: Expo screen undo history ===")

    # 1. Create a Stack object
    actions = Stack()

    # 2. Push 4 actions, in the order they happened
    for action in ["Bump order #101", "Bump order #102",
                   "Recall order #101", "Bump order #103"]:
        actions.push(action)
        print(f"Pushed: {action}")

    # 4. Demonstrate LIFO: the most recent action is on top and comes off first
    print(f"\nTop of stack (peek): {actions.peek()}")
    print("Undoing actions, newest first (LIFO):")
    while not actions.is_empty():
        print(f"  Undid: {actions.pop()}")

    # 5. Pop on an empty stack returns None instead of crashing
    print(f"\npop() on empty stack returned: {actions.pop()}")

    # 6. Peek on an empty stack also returns None
    print(f"peek() on empty stack returned: {actions.peek()}")

    # 7. Single-item stack: push one, pop one, confirm it is empty
    single = Stack()
    single.push("Bump order #200")
    print(f"\nSingle-item stack, popped: {single.pop()}")
    print(f"Is the stack empty now? {single.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: Kitchen order line ===")

    # 1. Create a Queue object
    orders = Queue()

    # 2. Enqueue 4 orders, in the order customers placed them
    for order in ["#101 Chicken sandwich", "#102 Pizza",
                  "#103 Burrito", "#104 Breakfast taco"]:
        orders.enqueue(order)
        print(f"Order received: {order}")

    # 4. Demonstrate FIFO: the oldest order is at the front and is cooked first
    print(f"\nNext order up (front): {orders.front()}")
    print("Cooking orders, oldest first (FIFO):")
    while not orders.is_empty():
        print(f"  Served: {orders.dequeue()}")

    # 5. Dequeue on an empty queue returns None instead of crashing
    print(f"\ndequeue() on empty queue returned: {orders.dequeue()}")

    # 6. Front on an empty queue also returns None
    print(f"front() on empty queue returned: {orders.front()}")

    # 7. Single-item queue: enqueue one, dequeue one, confirm it is empty
    single_q = Queue()
    single_q.enqueue("#200 Coffee")
    print(f"\nSingle-item queue, served: {single_q.dequeue()}")
    print(f"Is the queue empty now? {single_q.is_empty()}")


if __name__ == "__main__":
    main()