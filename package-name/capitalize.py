"""Capitalize module."""

# !/usr/bin/env python3

def capitalize(word):
    """Capitalize a word."""
    return f'{word[0].upper()}{word[1:]}' if word else ''
