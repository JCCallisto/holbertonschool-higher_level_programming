#!/usr/bin/env python3

from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass

class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return the sound a dog makes."""
        return "Bark"

class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return the sound a cat makes."""
        return "Meow"
