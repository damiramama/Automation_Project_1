from selenium import webdriver

Botanika_URL = "https://botanikabeauty.com/"
driver = webdriver.Chrome(executable_path="drivers/chromedriver_copy")
driver.get("https://botanikabeauty.com/")
driver.maximize_window()

#About Us buttom
aboutus_btn = driver.find_element_by_xpath('//a[@href="/pages/about-us"]')
aboutus_btn.click()

#Terms of Servise
terms_of_servise = driver.find_element_by_xpath('//a[@href="/pages/terms-of-service"]')
terms_of_servise.click()

# #Privacy Policy
privacy_policy = driver.find_element_by_xpath('//a[@href="/pages/privacy-policy"]')
privacy_policy.click()

driver.close()
driver.quit()
