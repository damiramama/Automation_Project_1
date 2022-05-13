from selenium import webdriver

Botanika_URL = "https://botanikabeauty.com/"
driver = webdriver.Chrome(executable_path="drivers/chromedriver_copy")
driver.get(Botanika_URL)
driver.maximize_window()


#About Us buttom
aboutus_btn = driver.find_element_by_xpath("(//*[contains(text(),'About Us')])[1]")
aboutus_btn.click()
get_current_url = driver.current_url
print("About Us Current URL = "+get_current_url)
driver.close()

driver = webdriver.Chrome(executable_path="drivers/chromedriver_copy")
driver.get(Botanika_URL)
driver.maximize_window()

#Terms of Servise
terms_of_servise = driver.find_element_by_xpath("//a[contains(text(),'Terms Of Service')]")
terms_of_servise.click()
get_current_url = driver.current_url
print("Terms and Conditions Current URL = "+get_current_url)
driver.close()

driver = webdriver.Chrome(executable_path="drivers/chromedriver_copy")
driver.get(Botanika_URL)
driver.maximize_window()

# #Privacy Policy
privacy_policy = driver.find_element_by_xpath("//a[contains(text(),'Privacy Policy')]")
privacy_policy.click()
get_current_url = driver.current_url
print("Privacy Policy Current URL = " + get_current_url)
driver.close()
driver.quit()
