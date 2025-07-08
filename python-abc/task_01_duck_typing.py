#!/usr/bin/env python3

class CountedIterator:
    """An iterator that keeps track of how many items have been iterated."""
    
    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0
    
    def __next__(self):
        """Return the next item and increment the counter."""
        item = next(self.iterator)
        self.count += 1
        return item
    
    def get_count(self):
        """Return the current count of items iterated."""
        return self.count
    
    def __iter__(self):
        """Return self to make the object iterable."""
        return self
