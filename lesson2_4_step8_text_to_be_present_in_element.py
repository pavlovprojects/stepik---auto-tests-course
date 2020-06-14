from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)
    # проверять в течение 12 секунд, пока цена не станет равна 100
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    # когда цена равна 100, нажать на кнопку book
    button = browser.find_element(By.ID, "book")
    button.click()
    # Код, который находит значение на странице
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # Заполнение поля ввода
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем результат
    button_submit = browser.find_element(By.ID, "solve")
    button_submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()


