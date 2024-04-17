# Importing the csv module for handling CSV files
import csv

# Function to calculate the average
def average(numbers):
    return sum(numbers) / len(numbers)

# Initializing variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
greatest_increase = {"date": None, "amount": float("-inf")}
greatest_decrease = {"date": None, "amount": float("inf")}

# Reading the CSV file
with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skipping the header row
    for row in reader:
        # Extracting date and profit/loss
        date = row[0]
        profit_loss = int(row[1])

        # Calculating total months and net total
        total_months += 1
        net_total += profit_loss

        # Calculating changes in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            # Checking for the greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Updating previous profit/loss
        previous_profit_loss = profit_loss

#average change
average_change = average(changes)

#results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Output of the analysis:
"""
Financial Analysis
------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""
