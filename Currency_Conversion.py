from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("E:/PyCharm Projects/chromedriver.exe")

#Hitting www.oanda.com
driver.get('https://www.oanda.com/currency/converter/#')
time.sleep(1)
#Find and click quote_currency_input box
From_search_box = driver.find_element_by_xpath('//input[@id="quote_currency_input"]')
time.sleep(1)
From_search_box.clear()

Curr_I_Have=input("Please enter Currency Code, which you have: ")

# Pass value to input box.
From_search_box.send_keys(Curr_I_Have)
time.sleep(1)
From_search_box.send_keys(Keys.RETURN)

#Find and click base_currency_input box.
To_search_box = driver.find_element_by_xpath('//input[@id="base_currency_input"]')
time.sleep(1)
To_search_box.clear()
Curr_I_Want=input("Please enter Currency Code, which you want: ")
# Pass search string on search box.
To_search_box.send_keys(Curr_I_Want)
time.sleep(1)
To_search_box.send_keys(Keys.RETURN)

#Find and click quote_amount_input box
From_Amt_box = driver.find_element_by_xpath('//input[@id="quote_amount_input"]')
time.sleep(1)
From_Amt_box.clear()
Amt_Exchange=input("Please enter amount, which you want to exchange: ")
# Pass to the input box.
From_Amt_box.send_keys(Amt_Exchange)
time.sleep(1)
From_Amt_box.send_keys(Keys.RETURN)
time.sleep(2)

#Find result amount tag element
Result_Amt = driver.find_element_by_xpath('//td[@id="sellMyCurrencyGet"]')

#User defined function for extracting a portion of string from a given string.
def get_str(resp_str,frm_str,to_str):
    start_index = resp_str.find(frm_str) + len(frm_str)
    end_index = resp_str.find(to_str, start_index)
    resp_dict = resp_str[start_index:end_index]
    return resp_dict

Result_amt = get_str((Result_Amt.text),'get ',' ')
print("{} {} is the exchanged price amount for you, from {} {}".format(Result_amt ,Curr_I_Want ,Amt_Exchange ,Curr_I_Have))
