import pandas as pd

# Load the dataset
import os

file_path = os.path.abspath('./Resources/election_data.csv')
print(file_path)  # Prints the absolute path to the console

data = pd.read_csv(file_path)

# Calculate the total number of months
total_months = data['Date'].count()

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" and the average of those changes
data['Change'] = data['Profit/Losses'].diff()
average_change = data['Change'].mean()

# Find the greatest increase in profits (date and amount)
greatest_increase = data.loc[data['Change'].idxmax()]

# Find the greatest decrease in profits (date and amount)
greatest_decrease = data.loc[data['Change'].idxmin()]

# Prepare the results
financial_analysis = {
    "Total Months": total_months,
    "Total": net_total,
    "Average Change": average_change,
    "Greatest Increase in Profits": (greatest_increase['Date'], greatest_increase['Change']),
    "Greatest Decrease in Profits": (greatest_decrease['Date'], greatest_decrease['Change']),
}

financial_analysis
import pandas as pd

# Load the dataset
file_path = 'budget_data.csv'
data = pd.read_csv(file_path)

# Calculate the total number of months
total_months = data['Date'].count()

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" and the average of those changes
data['Change'] = data['Profit/Losses'].diff()
average_change = data['Change'].mean()

# Find the greatest increase in profits (date and amount)
greatest_increase = data.loc[data['Change'].idxmax()]

# Find the greatest decrease in profits (date and amount)
greatest_decrease = data.loc[data['Change'].idxmin()]

# Prepare the results
financial_analysis = {
    "Total Months": total_months,
    "Total": net_total,
    "Average Change": average_change,
    "Greatest Increase in Profits": (greatest_increase['Date'], greatest_increase['Change']),
    "Greatest Decrease in Profits": (greatest_decrease['Date'], greatest_decrease['Change']),
}

# Print the results to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {financial_analysis['Total Months']}")
print(f"Total: ${financial_analysis['Total']}")
print(f"Average Change: ${financial_analysis['Average Change']:.2f}")
print(f"Greatest Increase in Profits: {financial_analysis['Greatest Increase in Profits'][0]} (${financial_analysis['Greatest Increase in Profits'][1]})")
print(f"Greatest Decrease in Profits: {financial_analysis['Greatest Decrease in Profits'][0]} (${financial_analysis['Greatest Decrease in Profits'][1]})")

# Export the results to a text file
output_file = 'financial_analysis.txt'
with open(output_file, 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {financial_analysis['Total Months']}\n")
    f.write(f"Total: ${financial_analysis['Total']}\n")
    f.write(f"Average Change: ${financial_analysis['Average Change']:.2f}\n")
    f.write(f"Greatest Increase in Profits: {financial_analysis['Greatest Increase in Profits'][0]} (${financial_analysis['Greatest Increase in Profits'][1]})\n")
    f.write(f"Greatest Decrease in Profits: {financial_analysis['Greatest Decrease in Profits'][0]} (${financial_analysis['Greatest Decrease in Profits'][1]})\n")

print(f"\nResults have been exported to {output_file}")
