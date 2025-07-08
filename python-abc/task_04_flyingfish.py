#!/usr/bin/env python3

class Fish:
    """Fish class representing aquatic animals."""

    def swim(self):
        """Method for swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Method describing fish habitat."""
        print("The fish lives in water")

class Bird:
    """Bird class representing flying animals."""

    def fly(self):
        """Method for flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Method describing bird habitat."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird."""

    def fly(self):
        """Override fly method for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method for flying fish."""
        print("The flying fish lives both in water and the sky!")
