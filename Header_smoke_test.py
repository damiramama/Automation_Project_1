from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Botanika_URL = "https://botanikabeauty.com/"

driver = webdriver.Chrome(executable_path="drivers/chromedriver_copy")
driver.get("https://botanikabeauty.com/")
driver.maximize_window()
get_url = driver.current_url
print(get_url)

#Signin button
signin_btn = driver.find_element_by_xpath('//span[@class="account-text"]')
signin_btn.click()

#Register button
register_btn = driver.find_element_by_xpath("//span[@class='register-text']")
register_btn.click()

#Language button
language_btn = driver.find_element_by_xpath('//span[@class="pre-currencies"]')
language_btn.click()
language_btn = driver.find_element_by_xpath('//a[@class="selected"]')
language_btn.click()

#Facebook button
facebook_btn = driver.find_element_by_xpath('//i[@class="icon-facebook"]')
# facebook_btn.is_displayed()
facebook_btn.click()

#obtain window handle of browser in focus
p = driver.current_window_handle
#obtain parent window handle
parent = driver.window_handles[0]
#obtain browser tab window
chld = driver.window_handles[1]
#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
#close browser tab window
driver.close()
#switch to parent window
driver.switch_to.window(parent)
print("Page title for parent window:")
print(driver.title)
#close browser parent window
driver.close()

# #Twitter button
driver = webdriver.Chrome(executable_path="drivers/chromedriver_copy")
driver.get("https://botanikabeauty.com/")
driver.maximize_window()
get_url = driver.current_url
print(get_url)

twitter_btn = driver.find_element_by_xpath('//i[@class="icon-twitter"]')
twitter_btn.is_displayed()
twitter_btn.click()

#obtain window handle of browser in focus
p = driver.current_window_handle
#obtain parent window handle
parent = driver.window_handles[0]
#obtain browser tab window
chld = driver.window_handles[1]
#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
#close browser tab window
driver.close()
#switch to parent window
driver.switch_to.window(parent)
print("Page title for parent window:")
print(driver.title)
#close browser parent window
driver.close()

#Instagram button
driver = webdriver.Chrome(executable_path="drivers/chromedriver_copy")
driver.get("https://botanikabeauty.com/")
driver.maximize_window()
get_url = driver.current_url
print(get_url)

instagram_btn = driver.find_element_by_xpath('//i[@class="icon-instagram"]')
instagram_btn.is_displayed()
instagram_btn.click()

instagram_url = driver.current_url
print(instagram_url)

#obtain window handle of browser in focus
p = driver.current_window_handle
#obtain parent window handle
parent = driver.window_handles[0]
#obtain browser tab window
chld = driver.window_handles[1]
#switch to browser tab
driver.switch_to.window(chld)
print("Page title for browser tab:")
print(driver.title)
#close browser tab window
driver.close()
#switch to parent window
driver.switch_to.window(parent)
print("Page title for parent window:")
print(driver.title)
#close browser parent window
driver.close()
driver.quit()