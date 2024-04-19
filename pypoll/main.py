import csv 
import os
csvpath = os.path.join("budget_data.csv")

csv_file = "election_data.csv"

total_votes = 0
candidates = {}

with open(csv_file, "r", newline='') as file:
    csv_reader = csv.reader(file)
    
    next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1

        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

winner = max(candidates, key=candidates.get)

print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)

output_file = "election_results.txt"
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-" * 30 + "\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-" * 30 + "\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-" * 30 + "\n")
    file.write(f"Winner: {winner}\n")
    file.write("-" * 30 + "\n")
