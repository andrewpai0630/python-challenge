import os
import csv
#path
budgetCSV = os.path.join("Resources", "budget_data.csv")
Budget = {}
Date = []
Revenue = []
sum = 0
#function
#def getData(budgetData):
    #totalMonths = len(Date)
#read
with open(budgetCSV, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        header  = next(csvreader)
        for row in csvreader:
            Date.append(row[0])
            Revenue.append(row[1])  
            sum = sum + int(row[1])
            NetRevenue = sum
        GreatestIncrease = max(row[1])
        GreatestDecrease = min(row[1])
        totalMonths = len(Date)
#print