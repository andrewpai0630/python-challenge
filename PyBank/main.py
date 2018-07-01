import os
import csv
#path
budgetCSV = os.path.join("budget_data.csv")
with open(budgetCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header  = next(csvreader)
    Date = []
    Revenue = []
    RevChange = []
    for row in csvreader:
        Date.append(row[0])
        Revenue.append(float(row[1]))
print("Financial Analysis")
print("------------------------------------")
print("Total Months: ", len(Date))
print("Total Revenue: ", sum(Revenue))
for i in range(1,len(Revenue)):
    RevChange.append(Revenue[i] - Revenue[i-1])
    AvgRevChange = str(sum(RevChange) / len(RevChange))
    MaxRevChange = str(max(RevChange))
    MinRevChange = str(min(RevChange))
    MaxRevChangeDate = str(Date[RevChange.index(max(RevChange))])
    MinRevChangeDate = str(Date[RevChange.index(min(RevChange))])
print("Average Revenue Change: $", AvgRevChange)
print("Greatest Increase in Revenue:",MaxRevChangeDate, "($",MaxRevChange,")")
print("Greatest Decrease in Revenue:", MinRevChangeDate, "($",MinRevChange,")")
with open("outputfile.txt",'w') as op:
        op.write("Financial Analysis:\n--------------------------------------------------\n")
        op.write("Total Months: "+str(len(Date))+"\n")
        op.write("Total Revenue: $"+str(sum(Revenue))+"\n")
        op.write("Average Change: $"+AvgRevChange+"\n")
        op.write("Greatest Increase In Profits: "+MaxRevChangeDate+"($"+MaxRevChange+")"+"\n")
        op.write("Greatest decrease in profits: "+MinRevChangeDate+"($"+MinRevChange+")"+"\n")








