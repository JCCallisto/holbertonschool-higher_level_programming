#!/usr/bin/env python3

class VerboseList(list):
    """A list subclass that prints notifications for modifications."""

    def append(self, item):
        """Add an item to the end of the list with notification."""
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, items):
        """Extend the list with multiple items with notification."""
        items_list = list(items)
        super().extend(items_list)
        print(f"Extended the list with {len(items_list)} items.")

    def remove(self, item):
        """Remove an item from the list with notification."""
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item from the list with notification."""
        if len(self) == 0:
            return super().pop(index)

        if index == -1:
            item = self[-1]
        else:
            item = self[index]

        result = super().pop(index)
        print(f"Popped {item} from the list.")
        return result
