import os 
import csv
VoterID = []
County = []
Candidate = []
#path
pollCSV = os.path.join("Resources", "election_data.csv")
#function
def election(voterData):
    print(f"Total vote: {str(totalVote)}")
#read
with open(pollCSV, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        VoterID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])
        totalVote = len(Candidate)
election


#print
