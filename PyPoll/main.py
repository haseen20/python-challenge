import os
import csv

# Path to the CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}

# Open the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header
    header = next(csvreader)
    
    # Loop through each row in the CSV
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        
        # Track votes for each candidate
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the percentage of votes for each candidate and the winner
winner = ""
max_votes = 0
results = []

for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Create the election results summary
election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
election_results += "\n".join(results)
election_results += (
    f"\n-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------"
)

# Print the results to the terminal
print(election_results)

# Save the results to a text file
with open('analysis/election_results.txt', 'w') as txt_file:
    txt_file.write(election_results)
