# Import from the pathlib and csv library
from pathlib import Path
import csv

# Set the file path
csvpath = Path('../../Instructions/PyBank/Resources/budget_data.csv')

# Initialise the variable to hold company returns
company_returns = []

# Initialise the line_num variable
line_num = 0

# Open the input path as a file object
with open(csvpath, 'r') as csvfile:
    
    # Print the datatype of the file object
    print(type(csvfile))
    
    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Print the datatype of the csvreader
    print(type(csvreader))
    
    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)
    line_num += 1
    
    # Print the header
    print(f"{header} <---- HEADER")
    
    # Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)
        # Set returns variable equal to the value in the 2nd column of each row
        returns = int(row[1])
        # Append the row returns value to the list of company returns
        company_returns.append(returns)

# Initialize metric variables
total_months = 0
total_return = 0
avg_return = 0
max_return = 0
min_return = 0

# Calculate the max, min, and average of the company returns
for returns in company_returns:
    
    # Sum the total and count variables
    total_return += returns
    total_months += 1
    
    # Logic to determine min and max returns
    if min_return == 0:
        min_return = returns
    elif returns > max_return:
        max_return = returns
    elif returns < min_return:
        min_return = returns

# Calculate the average returns
avg_return = total_return / total_months

# Set the output header
header = ["Max_Return", "Min_Return", "Avg_Return"]

# Create a list of metrics
metrics = [max_return, min_return, avg_return]

# Print results in terminal
print("                    ")
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total Return: ${total_return}")
print(f"Average Monthly Return: ${avg_return:.2f}")
print(f"Greatest Increase in Profits: ${max_return}")
print(f"Greatest Decrease in Profits: ${min_return}")

# Set the output file path
output_path = 'financial_analysis.txt'

# Open the output path as a file object
with open(output_path, 'w') as file:
    # Write financial analysis results to the output file, convert to string
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total Return: ${total_return}\n")
    file.write(f"Average Monthly Return: ${avg_return:.2f}\n")
    file.write(f"Greatest Increase in Profits: ${max_return}\n")
    file.write(f"Greatest Decrease in Profits: ${min_return}")
