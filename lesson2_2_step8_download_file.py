from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ivan_petrov@yandex.ru")

    # находим кнопку загрузки файла
    button_download_file = browser.find_element(By.ID, "file")
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    # файл для загрузки должен лежать в той же папке, что и исполняемый файл
    file_path = os.path.join(current_dir, 'file.txt')
    # применяем метод send_keys для загрузки файла
    button_download_file.send_keys(file_path)

    # Отправляем результат
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()