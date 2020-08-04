import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button_add_to_busket(browser):
    browser.get(link)
    time.sleep(30)
    button = len(browser.find_elements_by_css_selector("#add_to_basket_form .btn-add-to-basket"))
    assert button > 0, '!!!Not found!!!'

# pytest --language=es test_items.py
