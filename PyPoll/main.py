# This is the main script for the PyPoll challenge.
# Written by Jason Gabunilas


# import dependencies
import csv
import os

# create path to the data source file
csvpath = os.path.join('Resources', 'election_data.csv')

## Initialize important variables
# total votes
total_votes = 0

# placeholder for the most votes
most_votes = 0

# a dictionary that will contain candidate names as keys. Each candidate key will be paired with a dictionary that contains information about number of votes and percentage of total votes for that candidate
candidates_dict = {}

# open the file in read mode
with open(csvpath, mode = 'r', encoding = 'utf-8') as voting_info:
        
        # create the csvreader iterable
        csvreader = csv.reader(voting_info, delimiter=',')

        # Skip the header row
        csv_header = next(csvreader)

        for row in csvreader:
                # for every iteration through the loop, add another vote to the total_votes count
                total_votes += 1

                # check if the current candidate being voted for is already in the candidates dictionary. If not, add him/her to the dictionary with their name as the key and a dictionary as the value pair. For the dictionary, initialize 'votes' as a key and set the initial number of votes to 1 as its value pair.
                if row[2] not in candidates_dict:
                        candidates_dict[row[2]] = {"votes":1}

                # If the current candidate is already in the dictionary, then increment his/her vote count by 1 by calling that candidate's 'votes' key and incrementing the value by 1
                else:
                        candidates_dict[row[2]]["votes"] += 1

        # iterate through each candidate in the dictionary and create a new key:value pair that calculates the percentage of the total votes for that candidate. 

        for candidate in candidates_dict:
                candidates_dict[candidate]["percentage"] = (candidates_dict[candidate]["votes"] / total_votes) * 100
                # Additionally, determine whether the current candidate has more votes than the most_votes counter. If he/she does, update the most_votes variable to the number of votes for the current candidate and create/update the winner variable with that candidate's name
                if candidates_dict[candidate]['votes'] > most_votes:
                        most_votes = candidates_dict[candidate]['votes']
                        winner = candidate


## Print results to terminal
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
for candidate in candidates_dict:
        print(f"{candidate}: {candidates_dict[candidate]['percentage']:.03f}% ({candidates_dict[candidate]['votes']})")
print("---------------------------")
print(f"winner: {winner}")
print("---------------------------")

# Print all outputs to a text file and direct it into the analysis folder.

text_file = open(os.path.join('analysis/poll_data.txt'),'w')
print("Election Results", file = text_file)
print("---------------------------",file = text_file)
print(f"Total Votes: {total_votes}", file = text_file)
print("---------------------------", file = text_file)
for candidate in candidates_dict:
        print(f"{candidate}: {candidates_dict[candidate]['percentage']:.03f}% ({candidates_dict[candidate]['votes']})", file = text_file)
print("---------------------------", file = text_file)
print(f"winner: {winner}", file = text_file)
print("---------------------------", file = text_file)
text_file.close()