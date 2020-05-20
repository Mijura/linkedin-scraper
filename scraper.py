from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import os

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
    letters_links.append({"text": letters[i]. text, "href": letters[i].get_attribute('href')})
    i+=1

print(letters_links)
for letter in letters_links:
    print(letter)
    driver.get(letter["href"])
    l = letter["text"]

    elem = driver.find_elements_by_xpath("//*[@id=\"seo-dir\"]/div/div[3]/div/ul/li/*")

    if not os.path.exists('companies/'+str(l)):
        os.makedirs('companies/'+str(l))

    with open('companies/'+str(l)+'/'+str(l)+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Company name", "Linkedin"])

        i=1
        for company_link in elem:
            writer.writerow([i, company_link.text, company_link.get_attribute('href')])
            i+=1

    

driver.close()

