import pytest
from pytest import mark


@mark.UI
def test_myntra_function(chrome_browser):
    chrome_browser.get("https://www.myntra.com/")
    assert True