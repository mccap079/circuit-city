from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

driver = webdriver.Firefox()

currentStores = []

def get_store(address, uid):
	driver.get("https://maps.google.com/")
	time.sleep(6)
	searchbar = driver.find_element_by_css_selector('#searchboxinput')
	searchbar.send_keys(address)
	searchbar.send_keys(Keys.RETURN)
	time.sleep(5)
	try:
		driver.find_element_by_css_selector('.section-image-pack-button').click()
		time.sleep(5)
		driver.find_element_by_css_selector('#widget-zoom-out').click()
		time.sleep(1)
		driver.find_element_by_css_selector('#widget-zoom-out').click()
		time.sleep(1)
		driver.find_element_by_css_selector('#widget-zoom-out').click()
		time.sleep(15)
		imgName = 'img/' + str(uid) + '_street.png'
		driver.save_screenshot(imgName)
		time.sleep(3)
	except:
		imgName = 'img/' + str(uid) + '_street.png'
		driver.save_screenshot(imgName)
		time.sleep(3)
	try:
		currentStoreElem = driver.find_element_by_xpath("//h3[@class='section-result-title']/span")
		currentStore = driver.execute_script("return arguments[0].innerText;", currentStoreElem)
	except:
		currentStore = "";
	time.sleep(1)
	thisJsonObj = {'id': uid, 'address': address, 'currentStore': currentStore}
	currentStores.append(thisJsonObj)
	print str(uid) + ", " + currentStore

infile = open('locations_pretty.txt')
addresses = infile.readlines()

for i, address in enumerate(addresses):
	get_store(address, i)

with open('currentStores.json', 'w') as outfile:
 	json.dump(currentStores, outfile)

infile.close()