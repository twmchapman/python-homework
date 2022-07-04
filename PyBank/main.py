from pathlib import Path
import csv

csvpath = Path('../../Instructions/PyBank/Resources/budget_data.csv')

company_returns = []

line_num = 0

with open(csvpath, 'r') as csvfile:
    print(type(csvfile))
    
    csvreader = csv.reader(csvfile, delimiter=',')
          
    print(type(csvreader))
          
    header = next(csvreader)
    line_num += 1
          
    print(f"{header} <---- HEADER")
          
    for row in csvreader:
        print(row)
        returns = int(row[1])
        company_returns.append(returns)

total_months = 0
total_return = 0
avg_return = 0
max_return = 0
min_return = 0

for returns in company_returns:
    total_return += returns
    total_months += 1
    
    if min_return == 0:
        min_return = returns
    elif returns > max_return:
        max_return = returns
    elif returns < min_return:
        min_return = returns

avg_return = total_return / total_months

header = ["Max_Return", "Min_Return", "Avg_Return"]

metrics = [max_return, min_return, avg_return]

output_path = Path('output.csv')

with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(header)
    print(header)
    csvwriter.writerow(metrics)
    print(metrics)

print("                    ")
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total Return: ${total_return}")
print(f"Average Monthly Return: ${avg_return:.2f}")
print(f"Greatest Increase in Profits: ${max_return}")
print(f"Greatest Decrease in Profits: ${min_return}")

output_path = 'financial_analysis.txt'

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total Return: ${total_return}\n")
    file.write(f"Average Monthly Return: ${avg_return:.2f}\n")
    file.write(f"Greatest Increase in Profits: ${max_return}\n")
    file.write(f"Greatest Decrease in Profits: ${min_return}")
