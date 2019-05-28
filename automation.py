from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# This version is for Alena testing on Mac
#driver = webdriver.Chrome(executable_path="/Users/alenastankaitis/Desktop/chromedriver");
# driver = webdriver.Chrome(); # This is for use on Windows, be sure .exe is in same directory
driver.get("http://www.safeco.com")
assert "Safeco Insurance" in driver.title
elem = driver.find_element_by_name("location")
elem.clear()
elem.send_keys("60612")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
#driver.close()