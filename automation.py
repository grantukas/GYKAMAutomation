from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Edit this block depending on Mac/Windows
# This version is for Alena testing on Mac
#driver = webdriver.Chrome(executable_path="/Users/alenastankaitis/Desktop/chromedriver");
driver = webdriver.Chrome(); # This is for use on Windows, be sure .exe is in same directory

driver.get("http://www.safeco.com")
assert "Safeco Insurance" in driver.title
location = driver.find_element_by_name("location")
location.clear()
location.send_keys("60612")
location.send_keys(Keys.RETURN)

contactButton = driver.find_elements_by_class_name("contactBtn")
print(contactButton)

assert "No results found." not in driver.page_source
#driver.close()