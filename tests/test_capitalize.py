"""Testing module."""

# !/usr/bin/env python3

from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Unexpected output.')

if capitalize('') != '':
    raise Exception('Unexpected output.')

print('All tests passed successfully!')
