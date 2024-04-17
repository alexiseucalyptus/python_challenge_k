import csv

# Define the file path
file_path = "budget_data.csv"

# Initialize variables to store financial data
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_loss_changes = 0
months = 0

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Iterate over each row in the CSV
    for row in csvreader:
        # Extract data from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total number of months
        total_months += 1

        # Calculate net total amount of "Profit/Losses"
        net_total += profit_loss

        # Calculate change in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)

        # Update previous profit/loss
        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase in profits (date and amount)
greatest_increase = max(profit_loss_changes)
greatest_increase_index = profit_loss_changes.index(greatest_increase)
greatest_increase_date = months[greatest_increase_index]

# Find the greatest decrease in profits (date and amount)
greatest_decrease = min(profit_loss_changes)
greatest_decrease_index = profit_loss_changes.index(greatest_decrease)
greatest_decrease_date = months[greatest_decrease_index]

# Print the analysis results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Write the analysis results to a text file
with open("financial_analysis.txt", "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

