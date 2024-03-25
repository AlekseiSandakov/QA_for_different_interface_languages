from selenium.webdriver.common.by import By
import time


def test_different_languages(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(10)
    assert browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"), \
        'Кнопка добавить в корзину отсутсвует!'
