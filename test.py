
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with webdriver.Chrome() as browser:
	# 1. Регистрация
	browser.get('https://github.com/signup')
	time.sleep(2)  # Увеличенная пауза для полной загрузки страницы

	# 2. Поиск всех видимых полей ввода
	input_fields = browser.find_elements(
		By.CSS_SELECTOR,
		'input:not([type="hidden"]):not([aria-hidden="true"]), textarea'
	)

	# 3. Заполнение полей по ключу "Text"
	for field in input_fields:
		if field.is_displayed():
			field.clear()
			field.send_keys("Text")
			time.sleep(0.5)  # Пауза после каждого ввода

	# 4. Поиск и нажатие основной кнопки с увеличенной паузой
	time.sleep(1)  # Дополнительная пауза перед поиском кнопки
	button = browser.find_element(By.CSS_SELECTOR, 'button[data-continue-to="password-container"]')
	button.click()
	time.sleep(2)  # Увеличенная пауза после нажатия

	# 5. Поиск и нажатие финальной кнопки регистрации
	time.sleep(1)  # Дополнительная пауза перед поиском второй кнопки
	submit_button = browser.find_element(By.CSS_SELECTOR, 'button[data-continue-to="username-container"]')
	submit_button.click()
	time.sleep(2)  # Увеличенная пауза после нажатия

	# 6. Получение результата с увеличенным временем ожидания
	try:
		result_element = WebDriverWait(browser, 5).until(  # Увеличенное время ожидания
			EC.visibility_of_element_located((By.CSS_SELECTOR, '.error-message, .success-message'))
		)
		result_text = result_element.text
	except:
		result_text = "Сообщение не найдено в течение 5 секунд"

	# 7. Вывод результата
	print("Результат:", result_text)
	time.sleep(3)  # Пауза перед закрытием браузера
