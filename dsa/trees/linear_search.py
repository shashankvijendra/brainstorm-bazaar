class LinearSearchCollection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the collection."""
        self.items.append(item)

    def linear_search(self, target):
        """Perform a linear search for a target item in the collection."""
        for item in self.items:
            if item == target:
                return True
        return False

    def size(self):
        """Return the number of items in the collection."""
        return len(self.items)

# Example usage
if __name__ == "__main__":
    collection = LinearSearchCollection()

    # Adding items to the collection
    collection.add_item(10)
    collection.add_item(20)
    collection.add_item(30)
    collection.add_item(40)
    collection.add_item(50)

    # Performing a linear search for a specific item
    target_item = 30
    result = collection.linear_search(target_item)

    print(f"Item {target_item} found: {'Yes' if result else 'No'}")

    # Checking the size of the collection
    print(f"Number of items in the collection: {collection.size()}")
