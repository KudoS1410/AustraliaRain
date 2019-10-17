
import selenium.webdriver as wd
import time
from selenium.webdriver.common.keys import Keys

chrome_options = wd.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

browser = wd.Chrome(chrome_options = chrome_options)

browser.get('https://www.longpaddock.qld.gov.au/silo/')

choice = input('point-data?')

if int(choice) == 1:
    browser.get('https://www.longpaddock.qld.gov.au/silo/point-data/')

search_bars = browser.find_elements_by_xpath('//*[@placeholder = "dd/mm/yyyy"]')

search_bars

start_date = input('Start date in dd/mm/yyyy format:  ')

# entering in the start date field
search_bars[0].send_keys(start_date)

end_date = input('End date in dd/mm/yyyy format:  ')

# entering in the end date field
search_bars[1].clear()
search_bars[1].send_keys(Keys.CONTROL + "a")
search_bars[1].send_keys(Keys.DELETE)
search_bars[1].send_keys(end_date)

radios = browser.find_elements_by_class_name('radio')

radios[5].click()

search_bars = browser.find_elements_by_xpath('//*[@placeholder = "export_120416"]')

search_bars[0].send_keys('export1')

search_bars[0].send_keys(Keys.ENTER)


search_bars = browser.find_elements_by_xpath('//*[@placeholder = "Search on station name, station number or decimal latitude/longitude e.g. -27.63,152.71"]')


search_bars[0].send_keys('4001')

search_bars[0].send_keys(Keys.ENTER)


a = browser.find_elements_by_id('statioSelectSubmit')

a[0].click()


time.sleep(3)

browser.quit()





