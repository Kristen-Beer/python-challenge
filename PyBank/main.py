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
    for row in csv_reader:
        count += 1

print("Number of rows =", count)
