
from selenium import webdriver


driver = webdriver.Chrome(executable_path='drivers/chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()
new_registrant_btn = driver.find_element_by_xpath("//a[contains(text(), 'Continue')]")

#Getting the background color of the button
background_color = new_registrant_btn.value_of_css_property("background-color")
new_registrant_btn.click()

#Register Account
#Personal Details

firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.click()
firstname_input.send_keys("Iryna")

lasrname_input = driver.find_element_by_id("input-lastname")
lasrname_input.click()
lasrname_input.send_keys("Azimova")

email = "iryna.azimova5@gmail.com"
email_input = driver.find_element_by_id("input-email")
email_input.click()
email_input.send_keys(email)

phonenumber_input = driver.find_element_by_id("input-telephone")
phonenumber_input.click()
phonenumber_input.send_keys("412-482-0000")

#Address
address_input = driver.find_element_by_id("input-address-1")
address_input.click()
address_input.send_keys("134 Locust Ct")

city_input = driver.find_element_by_id("input-city")
city_input.click()
city_input.send_keys("Pittsburgh")

zone_input = driver.find_element_by_id("input-zone")
zone_input.click()
zone_input.send_keys("Pennsylvania")

state_input = driver.find_element_by_xpath("//option[@value='3663']")
state_input.click()

password = "123456"
pass_input = driver.find_element_by_id("input-password")
pass_input.click()
pass_input.send_keys(password)

verifypass_input = driver.find_element_by_id("input-confirm")
verifypass_input.click()
verifypass_input.send_keys(password)

checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")
checkbox.click()

continue_btn = driver.find_element_by_xpath("//input[@value='Continue']")
continue_btn.click()

click_muaccounts = driver.find_element_by_xpath("//a[@title='My Account']")
click_muaccounts.click()

succ_reg_continue_btn = driver.find_element_by_xpath("//a[@class='btn btn-primary']")
succ_reg_continue_btn.click()

driver.close()
driver.quit()

driver = webdriver.Chrome(executable_path='drivers/chromedriver')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

login_email = driver.find_element_by_id("input-email")
login_email.click()
login_email.send_keys(email)

login_pass = driver.find_element_by_id("input-password")
login_pass.click()
login_pass.send_keys(password)

login_btn = driver.find_element_by_xpath("//input[@value='Login']")
login_btn.click()

driver.close()
driver.quit()