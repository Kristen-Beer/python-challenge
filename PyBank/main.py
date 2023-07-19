#Find average change in Profits/losses
import csv

budgetdata_csv = r"C:\\Users\krism\Documents\School\Module3Challenge\python-challenge\Starter_Code\PyBank\Resources\\budget_data.csv"

# Open and read the csv
with open(budgetdata_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

    # Count months
    count = 0
    #variable to store the sum of the second column
    total_Profits_losses = 0
    #Variable to store the average change
    average_change = 0
    #variable to store the max profits/losses value
    greatest_increase = None

    
    for row in csv_reader:
        #Total months
        count += 1

        #Net total
        net_total = int(row[1])
        total_Profits_losses += net_total

        #Average change is the total / number of months
        average_change = int(row[1])
        final_average_change = int(total_Profits_losses/count)
        
    print("Financial Analysis")
    print("Total months =", count)
    print("Total:", total_Profits_losses)
    print("Average Change:", final_average_change)

    #Specify the file to write to
    