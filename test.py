from selenium import webdriver

browser = webdriver.Chrome()
url = "https://github.com/"
browser.get(url)
browser.quit()
