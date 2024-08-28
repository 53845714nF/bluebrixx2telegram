import pytest
import requests_mock

from bluebrixx import product_available

comingsoon_html = """
<div class='label_comingsoon' style='font-size: 1rem;'>Coming Soon</div>
"""

announcement_html = """
<div class='label_announcement' style='font-size: 1rem;'>Announcement</div>
"""

unavailable_html = """
<div class='label_unavailable'>Currently Not Available</div>
"""

available_html = """
<div class='product-details'>In Stock</div>
"""


def test_product_coming_soon(requests_mock):
    """
    Test for Status 'coming soon'
    """
    url = "https://www.bluebrixx.com/product/comingsoon"
    requests_mock.get(url, text=comingsoon_html)

    status, available = product_available(url)
    assert status == "coming soon"
    assert available is False


def test_product_announced(requests_mock):
    """
    Test for Status 'announced'
    """
    url = "https://www.bluebrixx.com/product/announced"
    requests_mock.get(url, text=announcement_html)

    status, available = product_available(url)
    assert status == "announced"
    assert available is False


def test_product_unavailable(requests_mock):
    """
    Test for Status 'currently not available'
    """
    url = "https://www.bluebrixx.com/product/unavailable"
    requests_mock.get(url, text=unavailable_html)

    status, available = product_available(url)
    assert status == "Currently not available"
    assert available is False


def test_product_available(requests_mock):
    """
    Test for Status 'Available'
    """
    url = "https://www.bluebrixx.com/product/available"
    requests_mock.get(url, text=available_html)

    status, available = product_available(url)
    assert status == "Available"
    assert available is True


def test_product_coming_soon_ignored(requests_mock):
    """
    Test für den Fall, dass 'font-size: 0.6rem' vorhanden ist und ignoriert werden soll
    """
    comingsoon_html_ignored = """
    <div class='label_comingsoon' style='font-size: 0.6rem;'>Coming Soon</div>
    """
    url = "https://www.bluebrixx.com/product/comingsoon-ignored"
    requests_mock.get(url, text=comingsoon_html_ignored)

    status, available = product_available(url)
    assert status == "Available"
    assert available is True


def test_product_available_valid_url(requests_mock):
    """
    Test that a valid BlueBrixx URL passes the check.
    """
    url = "https://www.bluebrixx.com/de/sets/1001234/Example-Product"
    requests_mock.get(url, text=unavailable_html)

    # Expecting no exception to be raised
    status, is_available = product_available(url)

    assert status == "Currently not available"
    assert not is_available


def test_product_available_invalid_url():
    """
    Test that an invalid BlueBrixx URL raises a ValueError.
    """
    url = "https://www.invalidsite.com/product/123"

    # Expecting a ValueError to be raised
    with pytest.raises(
        ValueError, match="URL must start with 'https://www.bluebrixx.com/'"
    ):
        product_available(url)
