import os
import csv

budgetdatacsv = os.path.join("budget_data.csv")

with open(budgetdatacsv, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	header = next(csvreader)
	total_months = 0
	total = 0
	profit_loss = []
	change = []
	date = []
	for row in csvreader:
		total_months = total_months + 1
		total = total + int(row[1])
		profitloss = int(row[1])
		profit_loss.append(profitloss)
		date.append(row[0])
	
	for x in range((total_months - 1)):
		change.append(profit_loss[x+1] - profit_loss[x])
		

print("Financial Analysis")
print("-------------------------------------")	
print(f"Total Months: {total_months}")
print(f"Total: ${total}")

average_change = round((profitloss - profit_loss[0]) / (total_months - 1), 2)
print(f"Average Change: ${average_change}")

greatest_increase = max(change)
max_index = ((change.index(greatest_increase)+1))
print(f"Greatest Increase in Profits: {(date[max_index])} (${greatest_increase})")

greatest_decrease = min(change)
min_index = ((change.index(greatest_decrease)+1))
print(f"Greatest Decrease in Profits: {(date[min_index])} (${greatest_decrease})")

output_file = os.path.join("print_as_file.txt")
with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis\n")
    datafile.write("-------------------------------------\n")
    datafile.write(f"Total Months: {total_months}\n")
    datafile.write(f"Total: ${total}\n")
    datafile.write(f"Average Change: ${average_change}\n")
    datafile.write(f"Greatest Increase in Profits: {(date[max_index])} (${greatest_increase})\n")
    datafile.write(f"Greatest Decrease in Profits: {(date[min_index])} (${greatest_decrease})\n")