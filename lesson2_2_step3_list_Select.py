from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

try:
    link = " http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который находит значение на странице
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    y = int(num1) + int(num2)

    # Инициализация нового объекта с тегом select
    select = Select(browser.find_element_by_tag_name("select"))
    # Ищем элемент с текстом "y"
    select.select_by_visible_text(str(y))

    # Отправляем результат
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()