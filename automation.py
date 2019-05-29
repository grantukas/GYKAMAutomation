from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def openContacts(contacts): # Function to open each contact in a list in a new tab
    for element in contacts:
        if(element.text == ""):
            continue # Skip if element is blank
        else:
            print(element.text) # Get element text and open in new tab, for Mac change CONTROL to COMMAND
            ActionChains(driver) \
                .key_down(Keys.CONTROL) \
                .click(element) \
                .key_up(Keys.CONTROL) \
                .perform()

def clickNext(): # Function to click the next button to use after searching for agencies
    navigationList = driver.find_element_by_xpath("//div[@class='simple-pagination compact-theme']")
    nextButton = navigationList.find_elements_by_tag_name("li")
    for element in nextButton:
        if (element.text == "Next"):
            element.click()


# Edit this block depending on Mac/Windows
# This version is for Alena testing on Mac
#driver = webdriver.Chrome(executable_path="/Users/alenastankaitis/Desktop/chromedriver");
driver = webdriver.Chrome() # This is for use on Windows, be sure .exe is in same directory as program

driver.get("http://www.safeco.com")
assert "Safeco Insurance" in driver.title
location = driver.find_element_by_name("location")
location.clear()
location.send_keys("60612")
location.send_keys(Keys.RETURN)

driver.implicitly_wait(5) # Wait for page to load

# Open each contact, then click next page
for i in range(5):
    driver.implicitly_wait(5)
    contactList = driver.find_elements_by_xpath("//a[contains(@href, '/find-an-insurance-agency/app/agency/')]")
    openContacts(contactList)
    clickNext()