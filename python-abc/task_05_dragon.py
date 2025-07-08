#!/usr/bin/env python3

class SwimMixin:
    """Mixin class that provides swimming functionality."""

    def swim(self):
        """Method for swimming behavior."""
        print("The creature swims!")

class FlyMixin:
    """Mixin class that provides flying functionality."""

    def fly(self):
        """Method for flying behavior."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits swimming and flying abilities from mixins."""

    def roar(self):
        """Method for dragon's roaring behavior."""
        print("The dragon roars!")
