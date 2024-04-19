import csv
import os

csv_path = os.path.join("budget_data.csv")

total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        total_months += 1

        profit_loss = int(row[1])

        total_profit_loss += profit_loss

        if previous_profit_loss != 0:
            profit_loss_change = profit_loss - previous_profit_loss

            profit_loss_changes.append(profit_loss_change)

            if profit_loss_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change
            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change


        previous_profit_loss = profit_loss

average_change = sum(profit_loss_changes) / len(profit_loss_changes)

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open("financial_analysis.txt", "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit_loss}\n")
    textfile.write(f"Average Change: ${round(average_change, 2)}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
