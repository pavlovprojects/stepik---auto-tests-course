from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который находит значение на странице
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    # Проверка, что атрибут valuex присутствует
    assert x is not None, "no valuex"
    y = calc(x)

    # Заполнение поля ввода
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Поиск и активация checkbox'а
    option1 = browser.find_element(By.ID,"robotCheckbox")
    option1.click()

    # Поиск и активация radiobitton'а по значению в атрибуте lable, в котором указан в атрибуте for id соответсвующего input'а
    option2 = browser.find_element(By.ID,"robotsRule")
    option2.click()

    # или
    # option2 = browser.find_element(By.CSS_SELECTOR,"[for='robotsRule']")
    # option2.click()

    # Отправляем результат
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()