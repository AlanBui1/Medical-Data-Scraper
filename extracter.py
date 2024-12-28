import csv

FILE = "bluebook.txt"

data = []
with open(FILE) as inFile:
    lines = inFile.readlines()
    
for line in lines:
    if len(line.strip().split()) == 1:
        continue
    try:
        name = line[:line.index(".")-1]
        lastperiod = line.rfind(".")-1
        money = ""
        while line[lastperiod] != " ":
            money += line[lastperiod]
            lastperiod -= 1
        money= money[::-1]
        money = money.replace(",", '')
        
        data.append([name, money])
    except:
        pass

csv_file = "output1.csv"


with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
