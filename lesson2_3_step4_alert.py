from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector(".btn.btn-primary")
    button1.click()

    # Переключение на окно с alert, подтверждение с помощью accept()
    alert = browser.switch_to.alert
    alert.accept()

    # Код, который находит значение на странице
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # Заполнение поля ввода
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем результат
    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()