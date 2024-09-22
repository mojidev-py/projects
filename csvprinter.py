import csv
import os

file1 = input("what .csv file do you want to open (enter the path to the file)")


with os.open(file1) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)