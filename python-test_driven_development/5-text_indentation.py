#!/usr/bin/python3

"""
Module for text formatting and indentation.

This module contains a function to format text with proper indentation after
specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints text with proper indentation after specific punctuation marks.
    
    The function prints the text character by character, and after each
    occurrence of '.', '?', or ':', it prints two new lines and skips
    any following spaces.

    Args:
        text (str): The text to be formatted and printed. Must be a string.

    Returns:
        None: This function prints the formatted text and
        doesn't return a value.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? Fine: thanks")
        Hello.
        <BLANKLINE>
        How are you?
        <BLANKLINE>
        Fine:
        <BLANKLINE>
        thanks

        >>> text_indentation("No punctuation here")
        No punctuation here

        >>> text_indentation("Multiple...   spaces?   after:   punctuation")
        Multiple.
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        spaces?
        <BLANKLINE>
        after:
        <BLANKLINE>
        punctuation

        >>> text_indentation()
        Traceback (most recent call last):
            ...
        TypeError: text_indentation() missing 1 required positional argument: 'text'

        >>> text_indentation(123)
        Traceback (most recent call last):
            ...
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            i += 1
