#!/usr/bin/env python3
# coding=utf-8

"""
Modul to check availability BlueBrixx products.
"""

from requests import get
from bs4 import BeautifulSoup


def product_available(url):
    """
    This function look for the status of products from BlueBrixx
    :param url: The URL of an BlueBrixx product.
    :return: status string and bool
    """

    response = get(url, timeout=5)
    html = BeautifulSoup(response.text, 'html.parser')

    # Determine status
    comingsoon_html = html.find(class_="label_comingsoon")
    announcement_html = html.find(class_="label_announcement")
    unavailable_html = html.find(class_="label_unavailable")

    # Try to filter the font-size: 0.6rem (Special Trick on the Website)
    try:
        if "font-size: 0.6rem" in comingsoon_html["style"]:
            comingsoon_html = None
    except:
        pass
    try:
        if "font-size: 0.6rem" in announcement_html["style"]:
            announcement_html = None
    except:
        pass

    # Processing the return values
    if comingsoon_html is not None:
        return 'coming soon', False
    if announcement_html is not None:
        return 'announced', False
    if unavailable_html is not None:
        return 'Currently not available', False

    return 'Available', True
