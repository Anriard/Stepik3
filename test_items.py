import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_if_add_button_is_here(browser):
    browser.get(link)
    button1 = len(browser.find_elements_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
    assert button1 > 0, 'No button'
    time.sleep(10)
