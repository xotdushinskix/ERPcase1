from selenium.webdriver.support.wait import WebDriverWait
import data
import unittest
from selenium import webdriver
from randomHelper import RandomHelper
import fillingFunctions
import searchFunctions



randomHelper = RandomHelper()



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.get('http://admin:q1w2e3r4@testing.bintime.com')
        self.driver.get('http://admin:skdf%24%23%26%26%25tg@erp.bintime.com:81/')

    def testLogin(self):
        driver = self.driver
        driver.maximize_window()

        #filling email field
        driver.find_element_by_xpath(data.emailField).send_keys(data.emailData)

        #filling password field
        driver.find_element_by_xpath(data.passwordField).send_keys(data.passwordData)

        #click on Login button
        driver.find_element_by_xpath(data.loginButton).click()

        driver.implicitly_wait(5)




        #go to Customer Management page
        self.navigateToCustomerManagement()
    def navigateToCustomerManagement(self):
        driver = self.driver

        #click on Customers button on manage menu
        driver.find_element_by_xpath(data.customersButton).click()

        #click on Customer Management button
        driver.find_element_by_xpath(data.customersManagementButton).click()

        driver.implicitly_wait(3)

        #click on Add Customer button
        driver.find_element_by_xpath(data.addCustomerButton).click()

        driver.implicitly_wait(3)




        # Customer Info
        self.fillingCustomerInfoFields()
    def fillingCustomerInfoFields(self):
        driver = self.driver

        #filling Customer Name field
        customerName = randomHelper.random_string_generator()
        driver.find_element_by_xpath(data.customerNameField).send_keys(customerName)

        #click on Status checkbox
        WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(data.statusCheckBox)).click()

        #select by Billing selected already

        #select random county by Billing Addresses
        fillingFunctions.selectDDRandomly(driver, data.counrtySDDListBilling, data.countrySelectDropDownTitleBilling)

        #filling Bill Address field
        randomBillAddressString = randomHelper.random_string_generator()
        randomBillAddressInt = randomHelper.random_int_generator()
        randomBillAddress = randomBillAddressString + ' ' + randomBillAddressInt
        driver.find_element_by_xpath(data.billAddressesField).send_keys(randomBillAddress)

        #select Shipping Addresses
        driver.find_element_by_xpath(data.addressesSelecrDropDown).click()
        driver.find_element_by_xpath(data.shippingAddressesXPath).click()

        driver.implicitly_wait(5)

        #select random country by Shipping Addresses
        fillingFunctions.selectDDRandomly(driver, data.counrtySDDListShipping, data.countrySelectDropDownTitleShipping)

        #filling Shipping Address field
        randomShippingAddressString = randomHelper.random_string_generator()
        randomShippingAddressInt = randomHelper.random_int_generator()
        randomShippingAddress = randomShippingAddressString + ' ' + randomShippingAddressInt
        driver.find_element_by_xpath(data.shippingAddressesField).send_keys(randomShippingAddress)

        #select random Customer Type
        fillingFunctions.selectDDRandomly(driver, data.customerTypeDropDown, data.customerTypeTitle)

        #select random Default Language
        fillingFunctions.selectDDRandomly(driver, data.defaultLanguageDropDown, data.defaultLanguageTitle)


        #filling Remarks field
        someRemarksStr = randomHelper.random_string_generator()
        someRemarksInt = randomHelper.random_int_generator()
        someRemarks = (someRemarksInt + ' ' + someRemarksStr + ' ') * 3
        driver.find_element_by_xpath(data.remarksField).send_keys(someRemarks)




        #Shipping Conditions
        self.shippinConditionMethod(customerName)
    def shippinConditionMethod(self, customerName):
        driver = self.driver

        fillingFunctions.shippingConditions(driver, data.shipCondDropDown, data.shipCondTitle, data.movMinimumField,
                                           data.movMaximumField, data.shippingCostsField,data.freeShippingFromField, data.pricePerItemField,
                                           data.flatFeeField, data.pricePerItemSecond, data.flatFeeSecond)




        # Other Info
        self.otherInfoMethod(customerName)
    def otherInfoMethod(self, customerName):
        driver = self.driver

        # Bonus name & Vat Percent fields
        fillingFunctions.otherInfo(driver, data.bonusNameField, data.vatPercentField)

        # Time Period from
        fillingFunctions.otherInfoTimePeriodFrom(driver, data.openCalendarFrom, data.calendarFromField)

        # Time Period to
        fillingFunctions.otherInfoTimePeriodTo(driver, data.openCalendarTo, data.calendarToField)




        # Contact Info
        self.contactInfoMethod(customerName)
    def contactInfoMethod(self, customerName):
        driver = self.driver

        fillingFunctions.contactInfo(driver, data.downArrow, data.contactName1, data.contactType1DD,
                                     data.contactType1Title, data.contactPhone1, data.contactWebSite)


        self.fillingEmail(customerName)
    def fillingEmail(self, customerName):
        driver = self.driver
        #filling Contact Email 1
        contEmailRandom = randomHelper.random_string_generator() + '@gmail.com'
        driver.find_element_by_xpath(data.contactEmail1).send_keys(contEmailRandom)

        # Purchase Info
        self.purchaseInfo(customerName, contEmailRandom)
    def purchaseInfo(self, customerName, contEmailRandom):
        driver = self.driver

        vatIDRandom = randomHelper.random_int_generator()
        driver.find_element_by_xpath(data.vatIDField).send_keys(vatIDRandom)

        # # Payment Terms select dd
        # fillingFunctions.selectDDRandomly(driver, data.paymentTermsDD, data.paymentTermsDDTitle)
        #
        # # Currency select dd
        # fillingFunctions.selectDDRandomly(driver, data.currencyDD, data.currencyDDTitle)

        # Price Model dd
        fillingFunctions.selectDDRandomly(driver, data.priceModelDD, data.priceModelDDTitle)


        self.saveCustomer(customerName, contEmailRandom, vatIDRandom)
    def saveCustomer(self, customerName, contEmailRandom, vatIDRandom):
        driver = self.driver

        #click on Save Customer button
        driver.find_element_by_xpath(data.saveCustomerButton).click()

        driver.implicitly_wait(5)

        try:
            driver.execute_script(" var globalFlasheMsg = [{'message':'Customer was successfully saved.','type':'success'}]; ")
            print('Customer successfully saved')
        except:
            print('Customer was not saved')




        self.makeSearchAfterAddNewCustomer(customerName, contEmailRandom, vatIDRandom)
    def makeSearchAfterAddNewCustomer(self, customerName, contEmailRandom, vatIDRandom):
        driver = self.driver

        #searching by Customer ID field
        customerID = searchFunctions.giveAnyField(driver, data.customerIDFieldFirst, data.customerIDFieldSecond)
        searchFunctions.searchInField(driver, data.customerIDColumnName, data.customerManagementSearchButton,
                                      data.customerIDField, customerID, data.customersManagementEmptySearchField,
                                      data.customerIDAfterSearch, data.customerManagementResetButton)

        #searching by Customer Name
        searchFunctions.searchInField(driver, data.customerNameColumnName, data.customerManagementSearchButton,
                                      data.customerNameFieldInSearching, customerName, data.customersManagementEmptySearchField,
                                      data.customerNameAfterSearch, data.customerManagementResetButton)


        #searching by Default Language
        # searchFunctions.searchInField(driver, data.defaultLanguageColumnName, data.customerManagementSearchButton,
        #                               data.defaultLanguageField, defLanguage, data.customersManagementEmptySearchField,
        #                               data.defaultLanguageAfterSearch, data.customerManagementResetButton)


        #searching by Contact Emails
        searchFunctions.searchInField(driver, data.contactEmailsColumnName, data.customerManagementSearchButton,
                                      data.contactEmailsField, contEmailRandom, data.customersManagementEmptySearchField,
                                      data.contactEmailsAfterSearch, data.customerManagementResetButton)



        #searching by VAT ID
        searchFunctions.searchInField(driver, data.vatIDColumnName, data.customerManagementSearchButton,
                                      data.vatIDFieldInSearching, vatIDRandom, data.customersManagementEmptySearchField,
                                      data.vatIDAfterSearch, data.customerManagementResetButton)

        print("Searching by Status make manually")


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
