class ListNode:
    def __init__(self, key, val, next_node=None):
        self.key = key
        self.val = val
        self.next = next_node


class MyHashMap:

    def __init__(self):
        # Array of buckets.
        # Each bucket stores a linked list to handle collisions.
        self.size = 1000
        self.buckets = [None] * self.size

    def _hash(self, key):
        # Map the key to a bucket index.
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self._hash(key)
        node = self.buckets[bucket]

        # Key already exists → update its value.
        while node:
            if node.key == key:
                node.val = value
                return
            node = node.next

        # Key doesn't exist → insert a new node at the head.
        new_node = ListNode(key, value, self.buckets[bucket])
        self.buckets[bucket] = new_node

    def get(self, key: int) -> int:
        bucket = self._hash(key)
        node = self.buckets[bucket]

        # Search the linked list in this bucket.
        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        bucket = self._hash(key)
        node = self.buckets[bucket]

        # Key is the first node in the bucket.
        if node and node.key == key:
            self.buckets[bucket] = node.next
            return

        # Search for the node and unlink it.
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
                return

            node = node.next