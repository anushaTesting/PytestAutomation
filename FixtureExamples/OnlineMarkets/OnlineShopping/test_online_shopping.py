from pytest import mark
import time

@mark.onlineshopping
def test_online_shopping(chrome_browser):
    first_browser = chrome_browser
    first_browser.get("https://www.amazon.in/")
    time.sleep(5)
    second_browser = chrome_browser
    second_browser.get("https://www.flipkart.com/")
    time.sleep(5)
    third_browser = chrome_browser
    third_browser.get("https://www.myntra.com/")
    assert True