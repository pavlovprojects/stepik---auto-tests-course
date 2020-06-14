from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button1.click()

    # Запоминаем имя текущей вкладки, чтобы можно было к ней вернуться
    current_window = browser.current_window_handle
    # Определяем имя новой вкладки
    new_window = browser.window_handles[1]
    # Переключаемся на новую вкладку
    browser.switch_to.window(new_window)

    # Код, который находит значение на странице
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # Заполнение поля ввода
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем результат
    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()