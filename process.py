import csv
import matplotlib.pyplot as plt

data = {}

MIN_MONEY = 150000 #exclude doctors below this amount

MAIN_SPECIALTIES = ['psychiatry',
        'cardiology',
        'critical care medicine',
        'radiology',
        'anesthesiology',
        'neurology',
        'dermatology',
        'respirology',
        'rheumatology',
        'obstetrics and gynecology',
        'infectious diseases',
        'neonatal-perinatal medicine',
        'plastic surgery',
        'hematology',
        'physical medicine and rehabilitation',
        'emergency medicine',
        'pediatric',
        'general surgery',
        'cardiac surgery']


data_file = "main_data.csv"

with open(data_file) as inFile:
    lines = inFile.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(",")

        money = int(lines[i][2])
        spec = lines[i][3].replace('Specialty practice - ','')
        for j in range(4, len(lines[i])):
            spec += ","+lines[i][j]
        spec = spec.replace('"','')
        
        if 'internal medicine' in spec and spec != 'internal medicine':
            spec = spec.replace('internal medicine, ', '').replace(', internal medicine','')

        for s in MAIN_SPECIALTIES:
            if s in spec:
                spec = s
                break

        if spec not in data and float(money) >= MIN_MONEY:
            data[spec] = []
        if float(money) >= MIN_MONEY:
            data[spec].append(money)

ret = []

for key in list(data.keys()):
    if len(data[key]) < 10:
        print(key)
        del data[key]

for i in data:
    NUM = len(data[i])
    REAL_AVG = sum(data[i]) // len(data[i])
    TOP_20_AVG = sum(data[i][: min(20, len(data[i]))]) // min(20, len(data[i]))
    MEDIAN = data[i][len(data[i]) // 2]
    MIDDLE_THIRD_AVG = sum(data[i][len(data[i])//3 : 2*len(data[i])//3]) // len(data[i][len(data[i])//3 : 2*len(data[i])//3])
    ret.append([i, NUM, REAL_AVG, TOP_20_AVG, MEDIAN, MIDDLE_THIRD_AVG])

#write data to csv
csv_file = "final.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(ret)

# function draw graphs
def plot(specialties, values, xlabel, ylabel, title):
    plt.bar(specialties, values, color='skyblue')
    for i, value in enumerate(values):
        plt.text(i, value + 1,  
                 str("{:.1e}".format(value))[:3], ha='center', va='bottom')  

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
        
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.5)  
    plt.show()


for i in data:
    data[i].sort(reverse=True)

MEANS = [[sum(data[i]) // len(data[i]), i] for i in data.keys()]
MEDIANS = [[data[i][len(data[i]) // 2], i] for i in data.keys()]
TOP_20_AVG = [[sum(data[i][: min(20, len(data[i]))]) // min(20, len(data[i])), i] for i in data.keys()]
TOP_QUARTILE = [[data[i][len(data[i]) // 4], i] for i in data.keys()]

MEANS.sort()
MEDIANS.sort()
TOP_20_AVG.sort()
TOP_QUARTILE.sort()

plot([i[1] for i in TOP_QUARTILE], [i[0] for i in TOP_QUARTILE], 'Specialties', 'Mean Billing Amount ($)', 'Mean Top Quartile Billing of Doctors in BC by Specialty')
plot([i[1] for i in MEANS], [i[0] for i in MEANS], 'Specialties', 'Mean Billing Amount ($)', 'Mean Billing of Doctors in BC by Specialty')
plot([i[1] for i in MEDIANS], [i[0] for i in MEDIANS], 'Specialties', 'Median Billing Amount ($)', 'Median Billing of Doctors in BC by Specialty')
plot([i[1] for i in TOP_20_AVG], [i[0] for i in TOP_20_AVG], 'Specialties', 'Top 20 Mean Billing Amount ($)', 'Top 20 Mean Billing of Doctors in BC by Specialty')
