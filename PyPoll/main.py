import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

voter = []
county = []
candidate = []

print("Election Results")
print("---------------------------")

with open(election_csv, 'r') as election_file:
    next(election_file)
    csvreader = csv.reader(election_file, delimiter=",")

    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])



total_voters = len(voter)
print(f"Total Voters: {total_voters}")
print("---------------------------")

Charles_count = candidate.count("Charles Casper Stockham")
charles_percent = Charles_count/len(candidate)*100
round_charles = round(charles_percent, 3)
print(f"Charles Casper Stockham: {round_charles}% ({Charles_count})")

Diana_count = candidate.count("Diana DeGette")
Diana_percent = Diana_count/len(candidate)*100
round_diana = round(Diana_percent, 3)
print(f"Diana DeGette: {round_diana}% ({Diana_count})")

Raymond_count = candidate.count("Raymon Anthony Doane")
raymond_percent = Raymond_count/len(candidate)*100
round_raymond = round(raymond_percent, 3)
print(f"Raymon Anthony Doane: {round_raymond}% ({Raymond_count})")

print("---------------------------")

winner = max(set(candidate), key = candidate.count)
print(f"Winner: {winner}")

print("---------------------------")

txt = open("election_result.txt", "w")
txt.write("Election Results" +"\n")
txt.write("---------------------------" +"\n")
txt.write(f"Total Voters: {total_voters}" +"\n")
txt.write("---------------------------" +"\n")
txt.write(f"Charles Casper Stockham: {round_charles}% ({Charles_count})" +"\n")
txt.write(f"Diana DeGette: {round_diana}% ({Diana_count})" +"\n")
txt.write(f"Raymon Anthony Doane: {round_raymond}% ({Raymond_count})" +"\n")
txt.write("---------------------------" +"\n")
txt.write(f"Winner: {winner}"+"\n")
txt.write("---------------------------" +"\n")