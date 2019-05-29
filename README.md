# GYKAM (Give Your Kid a Million) Automation

This Python program uses Selenium to automate searching through [Safeco](https://www.safeco.com) for life insurance providers.

Currently, the program opens the Safeco website in the Chrome browser, searches for independent agents by zipcode, then opens each agent's page in a new tab.

The goal of this project is to open each agent's contact information, navigate to their website, and save their contact information if they offer life insurance (if found on their website).

Functionalities that I am working on implementing:
* Save zip codes to search to a text file and parse the text file (save as a list), then search through zips
* Switch to each agent's tab and click their website button
  * If agent's website link is broken/blank, then output the name of the agent to a CSV (spreadsheet) and Google agent's info manually (or write another program to do that)
  * If agent's website link works, then search their website to see if they offer life insurance. If they do, save their contact info to the CSV

## Helpful links
* [Selenium documentation](https://selenium-python.readthedocs.io/)
* [Selenium WebDriver](https://www.seleniumhq.org/projects/webdriver/)
* [Selenium open tab, grab info, then return to main tab](https://gist.github.com/lrhache/7686903)
