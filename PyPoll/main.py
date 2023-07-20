import csv
#File path for csv:
election_data_csv = r'C:\\Users\krism\Documents\School\Module3Challenge\python-challenge\Starter_Code\PyPoll\Resources\\election_data.csv'

#Open and read the csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip the header row
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

    #Total number of votes cast
    count = 0
    #List all candidates names who received votes
    candidate_list = [] 
    candidate_votes = {}
    #Percentage of votes each candidate won
    percentage_of_votes = []
    #Total votes each candidate won
    votes_per_candidate = []
    #Winner based on popular vote
    winner_ = ""
    winning_count = 0


    #convert csv to dictionaries
    with open(election_data_csv) as election_data:
        reader = csv.DictReader(election_data)



    for row in reader:
        #Total votes
        count = count + 1

        #Grab each name
        candidate_name = row["Candidate"]
        #Add the name if it isn't in the list
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            #Track each candidate's votes
            candidate_votes[candidate_name] = 0

    #Add to the count of the votes
    candidate_votes[candidate_name] = candidate_votes[candidate_name]+1

    for candidate in candidate_votes

    print("Election Results")
    print(f"Total Votes: ", count)



    #Specify the file to write to
output_file_path = 'PyPoll\PyPoll_Analysis\PyPoll_Analysis.txt'
with open(output_file_path, 'w') as file:
    file.write("Election Results"+'\n')
    file.write("----------------------------"+'\n')
    file.write("Total Votes =" + str(count) +'\n')
    file.write("-----------------------------"+'\n')
 ')
   

    print('Output has been written to PyBank.txt successfully')
    




