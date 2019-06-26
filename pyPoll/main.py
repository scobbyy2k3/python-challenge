#import modules
import os
import csv
election_data = "Resources/election_data.csv"

# list names of candidates
candidates = []

# number of votes for each candidate
num_votes = []

# total number of votes
total_votes = 0

# percentage of total votes  for each candidate 
percent_votes = []



with open(election_data, newline = "") as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ",")
   csv_header = next(csvreader)

   for row in csvreader:
       # Count the total number of votes
       total_votes += 1
       
           

# Set the candidate names to candidatelist
       if row[2] not in candidates:
           candidates.append(row[2])
           index = candidates.index(row[2])
           num_votes.append(1)
       else:
           index = candidates.index(row[2])
           num_votes[index] += 1

      
# total vote count per candidate
   for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
# winner         
   winner = max(num_votes)
   index = num_votes.index(winner)
   winning_candidate = candidates[index]
    
 
# Election results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
for i in range(len(candidates)):
   print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")


#output to txt file
 # Name white file

write_election_datacsv = f"pyPoll_results.txt"

text = open("write_election_datacsv", mode = 'w')
text.write("Election Results\n")
text.write("---------------------------------------\n")
text.write(str(f"Total Votes: {str(total_votes)}\n"))
text.write("---------------------------------------\n")
for i in range(len(candidates)):
  
	text.write("---------------------------------------\n")
	text.write(str(f"Winner: {winning_candidate}"))
	text.write("---------------------------------------\n")

