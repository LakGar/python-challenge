import csv

# Path to the CSV file
file_path = './Resources/election_data.csv'

# Initialize a total vote counter and a dictionary for candidates
total_votes = 0
candidates = {}

# Open the CSV file and read the data
with open(file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Loop through each row
    for row in reader:
        # Increment the total vote count
        total_votes += 1
        
        # Get the candidate's name from the row
        candidate_name = row['Candidate']
        
        # If candidate is not in dictionary, add them with a vote count of 1
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            # Increment the candidate's vote count
            candidates[candidate_name] += 1

# Determine the winner
winner = max(candidates, key=candidates.get)

# Print and save the results
output = []
output.append("Election Results")
output.append("-------------------------")
output.append(f"Total Votes: {total_votes}")
output.append("-------------------------")

# Calculate the percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")

output.append("-------------------------")
output.append(f"Winner: {winner}")
output.append("-------------------------")

# Print the results
for line in output:
    print(line)

# Write the results to a text file
with open('election_results.txt', 'w') as txt_file:
    for line in output:
        txt_file.write(line + '\n')
