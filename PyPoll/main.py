import os
import csv

electiondatacsv = os.path.join("election_data.csv")

with open(electiondatacsv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	header = next(csvreader)
	total_votes = 0
	candidates = []
	
	for row in csvreader:
		total_votes = total_votes + 1
		candidates.append(row[2])

print("Election Results")
print("-------------------------------------")	
print(f"Total Votes: {total_votes}")
print("-------------------------------------")

dictionary = (dict((x,candidates.count(x)) for x in set(candidates)))

for k, v in dictionary.items():
	average = ((v / total_votes) * 100)
	print (f"{k}: {average : .3f}% ({v})")
	
for k, v in dictionary.items():
	if v == max(dictionary.values()):
		print("-------------------------------------")	
		print(f"Winner: {k}")
		print("-------------------------------------")	
		
output_file = os.path.join("print_as_file.txt")
with open(output_file, "w") as datafile:
	datafile.write("Election Results\n")
	datafile.write("-------------------------------------\n")	
	datafile.write(f"Total Votes: {total_votes}\n")
	datafile.write("-------------------------------------\n")
	dictionary = (dict((x,candidates.count(x)) for x in set(candidates)))
	for k, v in dictionary.items():
		average = ((v / total_votes) * 100)
		datafile.write(f"{k}: {average : .3f}% ({v})\n")
	for k, v in dictionary.items():
		if v == max(dictionary.values()):
			datafile.write("-------------------------------------\n")	
			datafile.write(f"Winner: {k}\n")
			datafile.write("-------------------------------------\n")	

