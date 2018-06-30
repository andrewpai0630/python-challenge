import os 
import csv
pollCSV = os.path.join("election_data.csv")
with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    VoterID = []
    County = []
    Candidate = []
    Candidate_choice = []
    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
print("Election Results")
print("-------------------------------------------")
print("Total Votes: ", len(VoterID)) 
print("-------------------------------------------")
for i in set(Candidate):
    Candidate_choice.append(Candidate.count(i))
Combined = dict(zip(set(Candidate), Candidate_choice))
sortedCandidate = (sorted(Combined.items(), key=lambda x: x[1], reverse=True))
with open("outputfile.txt",'w') as op:
    op.write("Election Results\n--------------------------------------------------\n")
    op.write("Total Votes: " + str(len(VoterID)) + "\n--------------------------------------------------\n")
    for i in range(len(sortedCandidate)):
        Name = str(sortedCandidate[i][0])
        Num = sortedCandidate[i][1]
        Total = len(VoterID)
        Percentage = round(((float(Num)/Total) * 100),3)
        print(Name + ": " + str(Percentage) + "%" + " (" + str(Num) + ")")
        op.write(str(sortedCandidate[i][0]) + ":" + str(round(((float(sortedCandidate[i][1])/Total) * 100),3)) + "%" + "(" + str(sortedCandidate[i][1]) + ")\n")
    print("-------------------------------------------")
    print("Winner: " + str(sortedCandidate[0][0]))
    print("-------------------------------------------")
    op.write("--------------------------------------------------\n" + "Winner: " + str(sortedCandidate[0][0]) + "\n--------------------------------------------------\n")
