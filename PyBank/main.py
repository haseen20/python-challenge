import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Lists to store data
dates = []
profits_losses = []
changes = []

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
greatest_increase = ["", 0]  # ["Date", amount]
greatest_decrease = ["", 0]  # ["Date", amount]

# Open the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Process each row
    for row in csvreader:
        # Add date to dates list
        date = row[0]
        profit_loss = int(row[1])
        
        # Track total number of months
        total_months += 1
        
        # Track net total profit/loss
        net_total += profit_loss
        
        # Calculate changes in profit/losses and track them
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            
            # Check for greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            
            # Check for greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease = [date, change]
        
        # Set previous profit/loss to current one for next iteration
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Prepare the analysis summary
analysis_summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the analysis summary
print(analysis_summary)

# Output the results to a text file in the analysis folder
with open('analysis/financial_analysis.txt', 'w') as analysis_file:
    analysis_file.write(analysis_summary)
