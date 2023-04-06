from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

grades = [[], []]
sleepTime = 0.2

class assignment:
    def __init__(self, assigned, due, category, score, points):
        self.assigned = assigned
        self.due = due
        self.category = category
        self.score = score
        self.points = points

class weights:
    def __init__(self, cat, weight):
        self.weigh = {}
        for i in cat:
            self.weigh[cat[cat.index(i)]] = weight[cat.index(i)]

class sclass:
    def __init__(self, assignments, weighting):
        self.assignments = assignments
        self.weighting = weighting

username = 'last.first'
password = '0000'

driver = webdriver.Chrome()
driver.get("https://md-allegany.myfollett.com/aspen/logon.do")
driver.find_element(by=By.NAME, value = "username").send_keys(username)
driver.find_element(by=By.NAME, value = "password").send_keys(password + Keys.ENTER)
time.sleep(sleepTime)
driver.find_element(by=By.XPATH, value = "//a[@title='Academics tab']").click()

s_classes = {}


time.sleep(sleepTime)
for classer in range(0, len(driver.find_elements(by=By.XPATH, value = "//td[@class='pointer']/a"))):
    c = driver.find_elements(by=By.XPATH, value = "//td[@class='pointer']/a")[classer - 1].text
    grades.append([])

    driver.find_elements(by=By.XPATH, value = "//td[@class='pointer']/a")[classer].click()
    time.sleep(sleepTime)

    driver.find_elements(by=By.XPATH, value = "//a[@title='List of assignments']")[0].click()
    time.sleep(sleepTime)
    driver.find_elements(by=By.XPATH, value = "//select[@id='gradeTermOid']")[0].click()
    driver.find_elements(by=By.XPATH, value = "//select[@id='gradeTermOid']/option")[0].click()
    time.sleep(sleepTime)


    def read_grades():
        an = -1
        for i in range(1, len(driver.find_elements(by=By.XPATH, value = "//div[@class='listGrid']/table/tbody/tr/td"))):
            x = str(driver.find_elements(by=By.XPATH, value = "//div[@class='listGrid']/table/tbody/tr/td")[i].text).replace('\n', '')
            if x == 'Select current record checkbox':
                an += 1
                aa.append([])
                pass
            
            x = x.split('%')
            if x[0] == 'Ungraded':
                x.append('')
            for i in range(0,len(x)):
                aa[an].append(x[i])
        
        grades[classer].append(aa)
            
            

    prange = range(0, len(driver.find_elements(by=By.XPATH, value = "//select[@title='Page list']/option")))
    

    for i in prange:
        aa = [[]]
        read_grades()
        
        driver.find_element(by=By.NAME, value = "nextPageButton").click()

    s_classes[c] = grades[classer]
    time.sleep(sleepTime)
    driver.find_elements(by=By.XPATH, value = "//a[@title='Details for a class']")[0].click()
    time.sleep(sleepTime)
    driver.find_elements(by=By.XPATH, value = "//button[@id='cancelButton']")[0].click()
    time.sleep(4)


with open('file.txt', 'w') as file:
    file.write(json.dumps(s_classes))
time.sleep(4)

driver.quit()
