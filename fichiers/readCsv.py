#  ouvrir le ficher
file = open("file1.csv","r")

#lire csv
import csv
reader = csv.reader(file,delimiter=";")


for line1 in reader:
    print(line1)

file = open("file1.csv","r")   
dicReader = csv.DictReader(file,delimiter=";")
for line2 in dicReader:
    print(line2)
