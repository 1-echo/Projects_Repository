import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#extract main urls

page_ext = requests.get("URL_PATH").text
soup_ext = BeautifulSoup(page_ext, "lxml")

urls1 = [] # list of all categories
for url_scan in soup_ext.find_all("li"):
    if len(list(url_scan.children)) == 1 and url_scan.a:
        urls1.append(url_scan.a["href"])

print("Number of extracted Urls: " + str(len(urls1)))

#start selenium

driver = webdriver.Chrome('PATH')

# va_start

nombre = []
info = []
direccion = []
telefono = []
web_page = []

#loop start main 1

for website_main in urls1:

    driver.get(website_main)
    sleep(random.uniform(3,5))

    # get the number of pages
    page_numbers = []
    try:
        loc = driver.find_elements(By.XPATH,value='//ul[@class="page-numbers"]')
        for data in loc:
            page_numbers.append(data.text)
        page_numbers = page_numbers[0].split()
    except:
        page_numbers.append(1)

    #search all the urls in all pages
    page_view = 1
    socios_urls = []
    while page_view < int(max(page_numbers))+1:
        try:
            sleep(random.uniform(5,7))
            button = driver.find_element(By.XPATH,value=('//span[@data-pageurl="{}"]').format(int(page_view)))
            button.click()
            sleep(random.uniform(5,7))
            loc = driver.find_elements(By.XPATH,value='//div[@class="col-md-6 lp-grid-box-contianer grid_view_s1 grid_view2 card1 lp-grid-box-contianer1 col-sm-12"]')
            for data in loc:
                socios_urls.append(data.get_attribute("data-posturl"))
            page_view += 1
        except:
            loc = driver.find_elements(By.XPATH,value='//div[@class="col-md-6 col-sm-12  lp-grid-box-contianer grid_view_s1 grid_view2 card1 lp-grid-box-contianer1"]')
            for data in loc:
                socios_urls.append(data.get_attribute("data-posturl"))
            page_view += 1

    print("Total Urls in subcategory= " + str(len(socios_urls)))
    for website_sub in socios_urls:

        driver.get(website_sub)
        sleep(random.uniform(8,10))
        # get the information and save in dataframe

        # nombre
        try:
            loc = driver.find_element(By.XPATH,value=('//div[@class="post-meta-left-box"]'))
            nombre.append(loc.find_element(By.XPATH,value=".//h1").text)
        except:
            nombre.append("No Data")
        # info
        try:
            info.append(driver.find_element(By.XPATH,value=('//div[@class="post-detail-content"]')).text)
        except:
            info.append("No Data")
        # direccion
        try:
            direccion.append(driver.find_element(By.XPATH,value=('//li[@class="lp-details-address"]')).text)
        except:
            direccion.append("No Data")
        # telefono
        try:
            telefono.append(driver.find_element(By.XPATH,value=('//li[@class="lp-listing-phone"]')).text)
        except:
            telefono.append("No Data")    
        # web_link
        try:
            web_page.append(driver.find_element(By.XPATH,value=('//li[@class="lp-user-web"]')).text)
        except:
            web_page.append("No Data")

    sleep(random.uniform(8,10))

temp = {'Nombre': nombre,
        'Información': info,
        'Dirección': direccion,
        'Telefonos': telefono,
        'Direccion Web': web_page}

reg = pd.DataFrame(temp)

reg.to_excel("data.xlsx")
