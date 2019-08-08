import pytest
from pytest import mark

@mark.UI
@mark.flipkart
def test_flipkart_function(chrome_browser):
    chrome_browser.get("https://www.flipkart.com/")
    assert True