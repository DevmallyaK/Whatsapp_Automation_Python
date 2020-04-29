from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r'D:/Softwares/chromedriver_win32/chromedriver.exe')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

target = input('Enter the name of user or group : ')

string = input('Enter your message : ')

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()

inp_xpath = '//div[@class="pluggable-input-body copyable-text selectable-text"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

for i in range(10):
    input_box.send_keys(string + Keys.ENTER)