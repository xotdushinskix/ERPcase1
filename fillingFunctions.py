import random
from datetime import datetime
from selenium.webdriver.support.select import Select
from randomHelper import RandomHelper

randomHelper = RandomHelper()




def selectDDRandomly(driver, dropDownXpathWithFullList, ddTitleXpath):
    selectRandomValue = Select(driver.find_element_by_xpath(dropDownXpathWithFullList))
    ddTitle = driver.find_element_by_xpath(ddTitleXpath).text
    ddTitle = str(ddTitle)
    a = [o.get_attribute('text') for o in selectRandomValue.options]
    randomValue = (random.choice(a))
    selectRandomValue.select_by_visible_text(randomValue)
    print('Selected ' + ddTitle + ' is ' + randomValue)




#Shipping Condition methods
def shippingConditions(driver, dropDownXpathWithFullList, ddTitleXpath, movMinimum, movMaximum, shipCostField,
                       freeShippingFromField, pricePerItemField, flatFeeField, pricePerItemFieldSecond, flatFeeSecondXpath):
    selectRandomValue = Select(driver.find_element_by_xpath(dropDownXpathWithFullList))
    ddTitle = driver.find_element_by_xpath(ddTitleXpath).text
    ddTitle = str(ddTitle)
    a = [o.get_attribute('text') for o in selectRandomValue.options]
    randomValue = (random.choice(a))
    selectRandomValue.select_by_visible_text(randomValue)
    print('Selected ' + ddTitle + ' is ' + randomValue)
    if randomValue == 'Minimum order value':

        help_varForMovMinimum = randomHelper.random_int_generator()
        help_varForMovMinimum = str(help_varForMovMinimum)
        varForMovMinimum = help_varForMovMinimum[:2]
        driver.find_element_by_xpath(movMinimum).send_keys(varForMovMinimum)
        help_varForMovMaximum = randomHelper.random_int_generator()
        help_varForMovMaximum = str(help_varForMovMaximum)
        varForMovMaximum = help_varForMovMaximum[:3]
        driver.find_element_by_xpath(movMaximum).send_keys(varForMovMaximum)
        help_shippingCosts = randomHelper.random_int_generator()
        help_shippingCosts = str(help_shippingCosts)
        shippingCosts = help_shippingCosts[:4]
        driver.find_element_by_xpath(shipCostField).send_keys(shippingCosts)
        help_freeShippingFromVar = randomHelper.random_int_generator()
        help_freeShippingFromVar = str(help_freeShippingFromVar)
        freeShippingFromVar = help_freeShippingFromVar[:4]
        driver.find_element_by_xpath(freeShippingFromField).send_keys(freeShippingFromVar)

    elif randomValue == 'Item based shipping (price per item)':
        help_pricePerItem = randomHelper.random_int_generator()
        help_pricePerItem = str(help_pricePerItem)
        pricePerItem = help_pricePerItem[:4]
        driver.find_element_by_xpath(pricePerItemField).send_keys(pricePerItem)

    elif randomValue == 'Flat fee per order':
        help_flatFee = randomHelper.random_int_generator()
        help_flatFee = str(help_flatFee)
        flatFee = help_flatFee[:3]
        driver.find_element_by_xpath(flatFeeField).send_keys(flatFee)

    elif randomValue == 'Item based shipping and flat fee per order':
        help_pricePerItemSecond = randomHelper.random_int_generator()
        help_pricePerItemSecond = str(help_pricePerItemSecond)
        pricePerItemSecond = help_pricePerItemSecond[:3]
        driver.find_element_by_xpath(pricePerItemFieldSecond).send_keys(pricePerItemSecond)
        help_flatFeeSecond = randomHelper.random_int_generator()
        help_flatFeeSecond = str(help_flatFeeSecond)
        flatFeeSecond = help_flatFeeSecond[:4]
        driver.find_element_by_xpath(flatFeeSecondXpath).send_keys(flatFeeSecond)




# Other Info filling method
def otherInfo(driver, bonusManeXpath, vatPercentXpath):
    #bonus name
    help_bonusNameRandom = randomHelper.random_string_generator()
    bonusNameRandom = help_bonusNameRandom[:6]
    driver.find_element_by_xpath(bonusManeXpath).send_keys(bonusNameRandom)

    #vat percent
    help_vatPercentRandom = randomHelper.random_int_generator()
    help_vatPercentRandom = str(help_vatPercentRandom)
    vatPercent = help_vatPercentRandom[:2]
    driver.find_element_by_xpath(vatPercentXpath).send_keys(vatPercent)

def otherInfoTimePeriodFrom(driver, calendarFromXpath, calendarFromField):
    driver.find_element_by_xpath(calendarFromXpath).click()
    i = datetime.now()
    firstTodayVar = i.strftime('%Y-%m-%d')
    driver.find_element_by_xpath(calendarFromField).send_keys(firstTodayVar)

def otherInfoTimePeriodTo(driver, calendarXpath, calendarField):
    driver.find_element_by_xpath(calendarXpath).click()
    i = datetime.now()
    secondTodayVar = ('2017-' + i.strftime('%m-%d'))
    driver.find_element_by_xpath(calendarField).send_keys(secondTodayVar)




# Contact Info
def contactInfo(driver, downArrowXpath, contName1Field, ddContactType,ddContactTypeTitleXpath, contPhone1Field,
                contWebSite1Field):
    driver.find_element_by_xpath(downArrowXpath).click()
    driver.implicitly_wait(3)
    #filling Contact Name 1
    contNameRandom = randomHelper.random_string_generator()
    driver.find_element_by_xpath(contName1Field).send_keys(contNameRandom)

    # select Contact Type 1
    selectRandomValue = Select(driver.find_element_by_xpath(ddContactType))
    ddContactTypeTitle = driver.find_element_by_xpath(ddContactTypeTitleXpath).text
    a = [o.get_attribute('text') for o in selectRandomValue.options]
    randomValue = (random.choice(a))
    randomValue = str(randomValue)
    selectRandomValue.select_by_visible_text(randomValue)
    print('Selected ' + ddContactTypeTitle + ' is ' + randomValue)

    # filling Contact Phone 1
    contPhoneRandom = randomHelper.random_int_generator()
    driver.find_element_by_xpath(contPhone1Field).send_keys(contPhoneRandom)


    #filling Contact Website 1
    contWebSite1Random = randomHelper.random_string_generator() + '.com'
    driver.find_element_by_xpath(contWebSite1Field).send_keys(contWebSite1Random)






