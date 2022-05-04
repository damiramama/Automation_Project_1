from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Botanika_URL = "https://botanikabeauty.com/"

driver = webdriver.Chrome(executable_path="drivers/chromedriver_copy")
driver.get("https://botanikabeauty.com/")
driver.maximize_window()

#Signin button
signin_btn = driver.find_element_by_xpath('//span[@class="account-text"]')
signin_btn.click()

#Register button
# driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
# driver.get("https://botanikabeauty.com/")
register_btn = driver.find_element_by_xpath('//span[@class="register-text"]')
register_btn.click()
#driver.close()

#Language button
language_btn = driver.find_element_by_xpath('//span[@class="pre-currencies"]')
language_btn.click()
language_btn = driver.find_element_by_xpath('//a[@class="selected"]')
language_btn.click()

#Facebook button
facebook_btn = driver.find_element_by_xpath('//i[@class="icon-facebook"]')
facebook_btn.click()

#Twitter button
twitter_btn = driver.find_element_by_xpath('//i[@class="icon-twitter"]')
twitter_btn.click()

#Instagram button
instagram_btn = driver.find_element_by_xpath('//i[@class="icon-instagram"]')
instagram_btn.click()

driver.close()
driver.quit()