# This is the main script for the PyBank challenge.
# Written by Jason Gabunilas

# import dependencies
import csv
import os

# create path to the Resources directory and bank information file (script must be run from the directory containing main.py)
csvpath = os.path.join('Resources', 'budget_data.csv')


## initialize the necessary values
# counter for total number of months in the dataset
month_counter = 0 
# counter for the net total profit/loss over the entire period
net_total = 0 
# A list to store the values of the profit/loss changes from one month to the next. 
changes = []
# A variable for total change, or the summation of month-to-month changes
total_change = 0
# A list to store the month with each iteration through the rows
months = []
# A placeholder for minimum change
min_change = 0
# A placeholder for maximum change
max_change = 0

# A dictionary that will hold the change in profit/loss : month pairs. We'll need this later to retrieve the biggest increase and decrease
change_month_dict = {}

# open the file in read mode
with open(csvpath, mode = 'r', encoding = 'utf-8') as bank_info:
        csvreader = csv.reader(bank_info, delimiter=',')

        # Skip the header row
        next(csvreader)
        
        for row in csvreader:
                # update the net total by adding the profit/loss of that month
                net_total += int(row[1])

                # The difference cannot be calculated for the first row since a previous row does not exist. Remember that the month counter starts at 0 and refers to the first line, and so we need to start the calculation when the month counter is 1 or greater
                if month_counter >= 1:
                        # Calculate the difference between the current month's profit/loss and the previous month's. If the previous month is 
                        monthly_difference = int(row[1]) - previous_amount
                        # print(f"Difference: {monthly_difference}")
                        # Append the monthly change to the changes list
                        changes.append(monthly_difference)

                        # Add the calculated difference to the change_month_dict dictionary as a key, with the month as a value
                        change_month_dict[monthly_difference] = row[0]

                # update the previous month's profit/loss to the current so that it carries into the next loop
                previous_amount = int(row[1])

                # append the current month to the months list
                months.append(row[0])
                
                # increment the month counter
                month_counter += 1

print('Financial Analysis')
print('-------------------------')
print(f"Total Months: {month_counter}")
print(f"Total: ${net_total}")

# Calculate the average change by iterating through the changes list, summing them up, and dividing by the total number of months
# print(changes)
for change in changes:
        total_change += change

        # Iterate through the changes list to find the minimum and maximum changes in profit/loss. Store those values in a variable so that they can be used later.
        if change > max_change:
                max_change = change
        elif change < min_change:
                min_change = change

# Calculate the average change. Remember that even though there are (month_counter) months, we only have (month_counter - 1) differences calculated.
average_change = total_change / (month_counter - 1)
print(f"Average Change: ${average_change:.2f}")

# Using the min and max changes found earlier, retrieve the months on which those changes occurred by tapping the change_month_dict dictionary
## DANGER!!! This method only works if there is only a single instance of maximum and minimum change
month_max_change = change_month_dict[max_change]
month_min_change = change_month_dict[min_change]

print(f"Greatest Increase in Profits: {month_max_change} (${max_change})")
print(f"Greatest Decrease in Profits: {month_min_change} (${min_change})")

# Print all outputs to a text file and direct it into the analysis folder.

text_file = open(os.path.join('analysis/financial_analysis.txt'),'w')

print('Financial Analysis', file = text_file)
print('-------------------------', file = text_file)
print(f"Total Months: {month_counter}", file = text_file)
print(f"Total: ${net_total}", file = text_file)
print(f"Average Change: ${average_change:.2f}", file = text_file )
print(f"Greatest Increase in Profits: {month_max_change} (${max_change})", file = text_file)
print(f"Greatest Decrease in Profits: {month_min_change} (${min_change})", file = text_file)

text_file.close()