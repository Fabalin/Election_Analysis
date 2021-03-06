# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize variable to hold the total votes PRIOR to opening the file
total_votes = 0
# Initialize empty LIST to hold candidate options
candidate_options = []
# Initialize empty dictionary to store each candidate's votes. key:candidate_name , value:vote_count 
candidate_votes = {}
# Initialize empty variables for winning candidate, count and percentage
winning_candidate = " "
winning_percentage = 0
winning_count = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Skip the header row.
    headers = next(file_reader)
    # Cycle through each row in the CSV file and count total votes.
    for row in file_reader:
        total_votes += 1
        # Declare new variable for each candidate's name 
        candidate_name = row[2]
        # Add each unique candidate's name to the candidate_options list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # Initialize each candidate's vote counts to 0 in dictionary
            candidate_votes[candidate_name] = 0
        # Increase each candidate's vote count by 1 while iterating through rows
        candidate_votes[candidate_name] += 1
# Open the output file to write the results. 
with open(file_to_save, "w") as txt_file:
  # Store the results in a variable 
  election_results = (
    f"\nElection Results\n"
    f"---------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"---------------------------\n")
  # The end= is the same as \n so anything printed after election results will be printed on a new line since the end= is an empty string.
  print(election_results, end="")
  # Save the final vote count to the text file. 
  txt_file.write(election_results)
  # Determine % votes per candidate and summarize each candidate's results
  # Iterate through candidate list
  for candidate_name in candidate_votes:
      # Retrieve vote count of a candidate.
      votes = candidate_votes[candidate_name]
      # Calculate the percentage of votes.
      vote_percentage = float(votes) / float(total_votes) * 100
      # Print candidate name and vote count and vote percentages for each candidate in separate lines.
      candidate_results = (
        f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
      print(candidate_results)
      # Write these results to the text file.
      txt_file.write(candidate_results)
      # Determine winning vote count and candidate
      # Determine if the vote count calculated is greater than winning count
      if votes > winning_count and vote_percentage > winning_percentage:
        # If true then set the vote count and percentage to the winning count and percentages
        winning_count = votes
        winning_percentage = vote_percentage
        # Set winning count equal to the variable candidate_name 
        winning_candidate = candidate_name
  # Print winning candidate and their vote count and percentage outside of the for loop.
  winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"---------------------------\n")
  print(winning_candidate_summary)
  # Write the results to the text file  
  txt_file.write(winning_candidate_summary)


