#autorization data
emailField = '//*[@id="UserLogin_username"]'
passwordField = '//*[@id="UserLogin_password"]'
emailData = 'admin'
passwordData = 'admin'
loginButton = '//*[@id="login-form"]//div[6]/input'




#manage menu data
customersButton = '//*[@id="top"]//nav/ul/li[6]/div/a'
customersManagementButton = '//*[@id="top"]//nav/ul/li[6]//li//a'




#data on Customer Management
addCustomerButton = '//*[@id="customer-grid"]//td[2]/a[2]'




# Create Customer page data
customerNameField = '//*[@id="Customer_customer_name"]'

statusCheckBox = '//*[@id="yw1"]//div[2]/div[2]//span'

addressesField = '//*[@id="Customer_addresses"]'

addressesSelecrDropDown = '//*[@id="Customer_addresses"]'
shippingAddressesXPath = '//*[@id="Customer_addresses"]//option[2]'

counrtySDDListBilling = '//*[@id="Customer_bill_country"]'
countrySelectDropDownTitleBilling = '//*[@id="bill_address"]//div[1]/label' #billing county
billAddressesField = '//*[@id="Customer_bill_address"]'

countrySelectDropDownTitleShipping = '//*[@id="shipping_addresses"]//div[1]/label[1]'
counrtySDDListShipping = '//*[@id="Customer_shipping_country"]'
shippingAddressesField = '//*[@id="Customer_shipping_addresses_address"]'

customerTypeDropDown = '//*[@id="Customer_customer_type"]'
customerTypeTitle = '//*[@id="yw1"]//div[7]/label[1]'

defaultLanguageDropDown = '//*[@id="Customer_selected_language_id"]'
defaultLanguageTitle = '//*[@id="yw1"]//div[8]/label[1]'

remarksField = '//*[@id="Customer_remarks"]'




#Shipping Condition data
shipCondDropDown = '//*[@id="Customer_shipping_conditions"]'
shipCondTitle = '//*[@id="yw2"]/div[2]/div[1]/label'

movMinimumField = '//*[@id="Customer_mov_min"]'
movMaximumField = '//*[@id="Customer_mov_max"]'
shippingCostsField = '//*[@id="Customer_mov_shipping_costs"]'
freeShippingFromField = '//*[@id="Customer_free_shipping"]'

pricePerItemField = '//*[@id="Customer_price_per_item"]'

flatFeeField = '//*[@id="Customer_flat_fee"]'

pricePerItemSecond = '//*[@id="Customer_price_per_item"]'
flatFeeSecond = '//*[@id="Customer_flat_fee"]'




# Other Info data
bonusNameField = '//*[@id="Customer_other_info_bonus_name"]'
vatPercentField = '//*[@id="Customer_other_info_vat_percent"]'

openCalendarFrom = '//*[@id="yw3"]//div[3]//div/span'
calendarFromField = '//*[@id="date-picker-1"]'
openCalendarTo = '//*[@id="yw3"]//div[4]//div/span'
calendarToField = '//*[@id="date-picker-2"]'




# Contact Info data
downArrow = '//*[@id="yw4"]//div[2]/div/div[1]'
contactName1 = '//*[@id="Customer_contacts_contact_name"]'
contactType1DD = '//*[@id="Customer_contacts_contact_type"]'
contactType1Title = '//*[@id="yw4"]//div[2]/label[1]'
contactPhone1 = '//*[@id="Customer_contacts_contact_phone"]'
contactEmail1 = '//*[@id="Customer_contacts_contact_email"]'
contactWebSite = '//*[@id="Customer_contacts_contact_website"]'




# Purchase Info data
vatIDField = '//*[@id="Customer_vat_id"]'

paymentTermsDD = '//*[@id="Customer_payment_terms"]'
paymentTermsDDTitle = '//*[@id="yw5"]//div[2]/div[2]/label'

currencyDD = '//*[@id="Customer_currency"]'
currencyDDTitle = '//*[@id="yw5"]//div[2]/div[3]/label'

priceModelDD = '//*[@id="Customer_price_model"]'
priceModelDDTitle = '//*[@id="yw5"]//div[2]/div[4]/label'



# Save Customer button
saveCustomerButton = '//*[@id="UpdateSave"]'



# Customer Management search button
customerManagementSearchButton = '//*[@id="customer-grid"]//tr/td[2]/button'
customerManagementResetButton = '//*[@id="reset-button-customer-grid"]'


#CustomerManagementEmptySearchField
customersManagementEmptySearchField = '//*[@id="customer-grid"]/div[1]/div'



#Customer id
customerIDFieldFirst = '//*[@id="customer-grid"]//tr['
customerIDFieldSecond = ']//a/span'
customerIDColumnName = '//*[@id="customer-grid_c0"]//a'
customerIDField = '//*[@id="Customer_customer_id"]'
customerIDAfterSearch = '//*[@id="customer-grid"]//td[1]/a/span'




#Customer Name
customerNameFieldFirst = '//*[@id="customer-grid"]//tr['
customerNameFieldSecond = ']/td[2]/a'
customerNameColumnName = '//*[@id="customer-grid_c1"]//a'
customerNameFieldInSearching = '//*[@id="Customer_customer_name"]'
customerNameAfterSearch = '//*[@id="customer-grid"]//table[2]//tr[1]/td[2]/a'



#Default Language
defaultLanguageFirst = '//*[@id="customer-grid"]//tr['
defaultLanguageSecond = ']/td[3]/a'
defaultLanguageColumnName = '//*[@id="customer-grid_c2"]//a'
defaultLanguageField = '//*[@id="Customer_selected_language_id"]'
defaultLanguageAfterSearch = '//*[@id="customer-grid"]//tr[1]/td[3]/a'



#VAT ID
vatIDFirst = '//*[@id="customer-grid"]//tr['
vatIDSecond = ']/td[5]/a'
vatIDColumnName = '//*[@id="customer-grid_c4"]//a'
vatIDFieldInSearching = '//*[@id="Customer_vat_id"]'
vatIDAfterSearch = '//*[@id="customer-grid"]//tr[1]/td[5]/a'


#Contact Emails
contactEmailsFirst = '//*[@id="customer-grid"]//tr['
contactEmailsSecond = ']/td[4]/a'
contactEmailsColumnName = '//*[@id="customer-grid_c3"]'
contactEmailsField = '//*[@id="Customer_contacts_search"]'
contactEmailsAfterSearch = '//*[@id="customer-grid"]//tr[1]/td[4]/a'
