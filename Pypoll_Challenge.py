# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
counties = []
countyVotes = {} # sorry, i am a camelCase die hard

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largestCounty = ""
countyHighestTurnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        # 4a, 4b, 4c, 5 done here
        county = row[1]
        if county not in counties:
            # add the new county to the county list and countyVotes dict
            counties.append(county)
            countyVotes[county] = 0
        
        # increment the county's vote total
        countyVotes[county] += 1

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)
    # 6a: Write a for loop to get the county from the county dictionary.
    for countyName in [key for key in countyVotes.keys()]:
        # 6b: Retrieve the county vote count.
        countyVoteTotal = countyVotes[countyName]
        # 6c: Calculate the percentage of votes for the county.
        countyTurnoutPercent = countyVoteTotal / (sum([value for value in countyVotes.values()])) * 100

         # 6d: Print the county results to the terminal.
         # this is the worst way to get a substring I can think of but I'm tired
        countyResults = (countyName + ' county: ' + str(countyTurnoutPercent)[0:5] + '% (' + str(countyVoteTotal) + ')\n')
        print(countyResults)
         # 6e: Save the county votes to a text file.
        txt_file.write(countyResults)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (countyVotes[countyName] == max([value for value in countyVotes.values()])):
            turnoutMsg = ('\nHighest Turnout: ' + countyName + ' county, with ' + str(countyVotes[countyName]) + ' votes\n\n')

    # 7: Print the county with the largest turnout to the terminal.
    print(turnoutMsg)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(turnoutMsg)

    # Save the final candidate vote count to the text file.

    candidate_results = (
            f"Candidate Results:\n"
            f"-------------------------\n")
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results += (
            f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # print the candidate results and save to text file
    print(candidate_results)
    txt_file.write(candidate_results)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.2f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
