import csv


with open('comments_Qo8dXyKXyME_01-12-2023.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['textOriginal'])


with open('comments_h7_T88PbJMs_01-12-2023.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['textOriginal'])


with open('comments_oCPi3MUcAdQ_01-12-2023.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['textOriginal'])