import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

##driver = webdriver.Chrome()  
##driver.get("https://www.cpsbc.ca/public/registrant-directory")
##
##link = driver.find_element(By.CSS_SELECTOR, "label.option.custom-control-label")  
##link.click()
##
###filter to only get specialists
##buttons = driver.find_elements(By.CLASS_NAME, "custom-control-label")
##for button in buttons:
##    if "Specialists" in button.text.strip():  
##        button.click()  
##        break  
##search = driver.find_element(By.ID, "edit-ps-submit")
##search.click()
##time.sleep(10)
##
##
##data = {}
##NUM_PAGES = 989
##
##for i in range(NUM_PAGES):
##    time.sleep(5)
##    items = driver.find_elements(By.CLASS_NAME, "result-item")
##
##    for item in items:
##        name = ""
##        spec = ""
##        for element in item.find_elements(By.XPATH, ".//*"):
##            #get name of doctor
##            if element.tag_name == "h5": 
##                name = element.text.replace("arrow_forward", "").strip()
##
##            #get specialty of doctor
##            if "Practice type:" in element.text and element.text.strip() != "Practice type:":
##                spec = element.text.replace("Practice type: ", "")
##                
##        if name != "" and spec != "":
##            data[name] = spec
##
##    #go to next page
##    arrow = driver.find_element(By.CLASS_NAME, "fa-caret-right")
##    arrow.click()
##
##    #update file with data
##    with open("doctor_data.json", "w") as file:
##        json.dump(data, file, indent=4)  # 'indent' makes the JSON file readable


with open("doctor_data.json", "r") as file:
    data = json.load(file)

newdata = []

with open("output1.csv") as inFile:
    lis = inFile.readlines()
    for i in range(len(lis)):
        lis[i] = lis[i].strip().split(",")
        lis[i][0] = lis[i][0].replace('"', '')
        lis[i][1] = lis[i][1].replace('"', '')

        name = lis[i][0] +","+lis[i][1]
        
        if name in data:
            lis[i].append(data[name])
            newdata.append(lis[i])

csv_file = "main_data.csv"

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(newdata)
