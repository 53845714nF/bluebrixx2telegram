#!/usr/bin/env python3
# coding=utf-8

"""
Tool that prints the BlueBrixx product status.
"""

from bluebrixx import product_available
from os import getenv


class UnconfiguredEnvironment(Exception):
    """base class for new exception"""
    pass


if not getenv('PRODUCT_URL', None):
    raise UnconfiguredEnvironment

PRODUCT_URL = getenv('PRODUCT_URL')
text, boolean = product_available(PRODUCT_URL)

print(f'The product is { text }.')
