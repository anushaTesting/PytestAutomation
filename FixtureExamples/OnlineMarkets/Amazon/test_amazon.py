import pytest
from pytest import mark


@mark.UI
def test_amazon_function(chrome_browser):
    chrome_browser.get("https://www.amazon.in/")
    assert True