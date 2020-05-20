from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import os
import time

if not os.path.exists('companies'):
    os.makedirs('companies')

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/directory/companies/")
elem = driver.find_elements_by_class_name("form-toggle")
elem[1].click()

elem = driver.find_element_by_id("login-email")
elem.send_keys("miodragvilotijevic@gmail.com")


elem = driver.find_element_by_id("login-password")
elem.send_keys(os.environ['link'])


elem = driver.find_element_by_id("login-submit")
elem.submit()

letters = driver.find_elements_by_xpath("//*[@id=\"seo-dir\"]/div/div[2]/div/ol/li/*")

i = 0
letters_links=[]
while(i<len(letters)):
    letters_links.append({"text": letters[i].text, "href": letters[i].get_attribute('href')})
    i+=1

for letter in letters_links:

    driver.get(letter["href"])
    l = letter["text"]

    if not os.path.exists('companies/'+str(l)):
        os.makedirs('companies/'+str(l))

    pages = driver.find_elements_by_xpath("//*[@id=\"seo-dir\"]/div/div[4]/div/ol/li/*")
    
    i = 0
    pages_links=[]
    while(i<len(pages)):
        pages_links.append({"text": pages[i].text, "href": pages[i].get_attribute('href')})
        i+=1

    for page in pages_links:

        driver.get(page["href"])

        elem = driver.find_elements_by_xpath("//*[@id=\"seo-dir\"]/div/div[3]/ul/li/*")
        with open('companies/'+str(l)+'/'+page["text"]+'.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Company name", "Linkedin"])

            i=1
            for company_link in elem:
                writer.writerow([i, company_link.text, company_link.get_attribute('href')])
                i+=1

    

driver.close()

