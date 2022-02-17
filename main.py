from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv


chromedriver = "D:\chromedriver"
driver = webdriver.Chrome(chromedriver)

#xpaths for first page
before_ques1 = "/html/body/div[1]/div/div[5]/div["
after_ques1 = "]/table/tbody/tr[1]/td[2]/p"

before1 = "/html/body/div[1]/div/div[5]/"
after1 = "/table/tbody/tr[2]/td/div[4]/a[1]"

before_ans1 = "/html/body/div[1]/div/div[5]/div["
after_ans1 = "]/table/tbody/tr[2]/td/div[1]/p[1]/span[2]"

#xpaths for middle pages
#ques
before_ques = "/html/body/div[1]/div/div[4]/div["
after_ques = "]/table/tbody/tr[1]/td[2]/p"

#View Answer click
before = "/html/body/div[1]/div/div[4]/"
after = "/table/tbody/tr[2]/td/div[4]/a[1]"

#ques
before_ans = "/html/body/div[1]/div/div[4]/div["
after_ans = "]/table/tbody/tr[2]/td/div[1]/p[1]/span[2]"



#xpaths for last page
before_ques2 = "/html/body/div[1]/div/div[4]/div["
after_ques2 = "]/table/tbody/tr[1]/td[2]/p"

before2 = "/html/body/div[1]/div/div[4]/"
after2 = "/table/tbody/tr[2]/td/div[4]/a[1]"


before_ans2 = "/html/body/div[1]/div/div[4]/div["
after_ans2 = "]/table/tbody/tr[2]/td/div[1]/p[1]/span[2]"


ans = []
ques = []
options = []

#first pg extraction
page = "https://www.indiabix.com/general-knowledge/basic-general-knowledge/"
driver.get(page)
time.sleep(5)
for i in range(3, 9):
    xpath = before_ques1 + str(i) + after_ques1
    ques.append(driver.find_element_by_xpath(xpath).text)
    a = ""
    for k in range(1, 5):
        xpath = "/html/body/div[1]/div/div[5]/div[" + str(i) + "]/table/tbody/tr[2]/td/table/tbody/tr[" + str(
            k) + "]/td[2]"
        a += driver.find_element_by_xpath(xpath).text + ","
    options.append(a)
    xpath = before1 + "div[" + str(i) + "]" + after1
    driver.find_element_by_xpath(xpath).click()
    time.sleep(0.5)
    xpath = before_ans1 + str(i) + after_ans1
    ans.append(driver.find_element_by_xpath(xpath).text)
    time.sleep(0.8)


#middle pages extraction
for j in range(2,13):
    if j<10:
        page = "https://www.indiabix.com/general-knowledge/basic-general-knowledge/00500"
    else:
        page = "https://www.indiabix.com/general-knowledge/basic-general-knowledge/0050"
    driver.get(page+str(j))
    time.sleep(5)
    for i in range(3,9):
        xpath = before_ques + str(i)+ after_ques
        ques.append(driver.find_element_by_xpath(xpath).text)
        a = ""
        for k in range(1,5):
            xpath = "/html/body/div[1]/div/div[4]/div["+str(i)+"]/table/tbody/tr[2]/td/table/tbody/tr["+str(k)+"]/td[2]"
            a += driver.find_element_by_xpath(xpath).text + ","
        options.append(a)
        xpath = before + "div[" + str(i)+ "]"+after
        driver.find_element_by_xpath(xpath).click()
        time.sleep(0.5)
        xpath = before_ans + str(i) + after_ans
        ans.append(driver.find_element_by_xpath(xpath).text)
        time.sleep(0.8)

#last pg extraction
page = "https://www.indiabix.com/general-knowledge/basic-general-knowledge/005013"
driver.get(page)
time.sleep(5)
for i in range(3, 8):
    xpath = before_ques2 + str(i) + after_ques2
    ques.append(driver.find_element_by_xpath(xpath).text)
    a = ""
    for k in range(1, 5):
        xpath = "/html/body/div[1]/div/div[4]/div[" + str(i) + "]/table/tbody/tr[2]/td/table/tbody/tr[" + str(
            k) + "]/td[2]"
        a += driver.find_element_by_xpath(xpath).text + ","
    options.append(a)
    xpath = before2 + "div[" + str(i) + "]" + after2
    driver.find_element_by_xpath(xpath).click()
    time.sleep(0.5)
    xpath = before_ans + str(i) + after_ans
    ans.append(driver.find_element_by_xpath(xpath).text)
    time.sleep(0.8)

#csv input
with open('IndiaBixGK.csv','w+') as f:
    writer = csv.writer(f)
    for i in range(len(ques)):
        writer.writerow([ques[i],ans[i],options[i]])