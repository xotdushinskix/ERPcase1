import random
from selenium.webdriver.common.keys import Keys


def giveAnyField(driver, firstXpathPiece, secondXpathPiece):
    help_a = 1
    resXpath = []
    while help_a <= 8:
        try:
            help_a += 1
            help_b = help_a
            help_b = str(help_b)

            frst = firstXpathPiece
            scnd = secondXpathPiece
            fullXpath = frst + help_b + scnd
            textWeb = driver.find_element_by_xpath(fullXpath).text
            resXpath.append(textWeb)
        except:
            pass
    return random.choice(resXpath)


def searchInField(driver, searchingColumnName, searchButton, searchField, someData, emptySearchField, resultAfterSearch, resetButton):
    columnName = driver.find_element_by_xpath(searchingColumnName).text
    driver.find_element_by_xpath(searchButton).click()
    driver.find_element_by_xpath(searchField).send_keys(someData)
    driver.find_element_by_xpath(emptySearchField).send_keys(Keys.ENTER)
    driver.implicitly_wait(3)
    resAfterS = driver.find_element_by_xpath(resultAfterSearch).text
    driver.implicitly_wait(2)
    if resAfterS == someData:
        print('Searching by ' + columnName + ' successfully worked')
    else:
        print('Searching by ' + columnName + ' was not worked')
        printDataForFielSuccessfullyDisplayed = '/home/nikita/SeleniumERP/ERPcase1/' + 'search_by_field_' + columnName + 'was_not_worked'
        driver.save_screenshot(printDataForFielSuccessfullyDisplayed)
    driver.find_element_by_xpath(searchButton).click()
    driver.find_element_by_xpath(resetButton).click()
