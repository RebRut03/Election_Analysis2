# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each cadidate won
# 4. The total number of votes each cadidate won
# 5. The winner of the electoin based on popular vote.


# Add our dependencies
import csv
import os

# Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and Print the header row
    headers = next(file_reader)
    print(headers)

 

