import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    # List for vote ids
    vote_ids = []
    # Dictionary for cadidates and votes
    candidates = {}

    # for loop to loop through .csv file rows
    def vote_analyze():
        print("Election Results")
        print("-------------------------")
        for row in csvreader:
            vote_ids.append(row[0])
            candidates[row[2]] = candidates.get(row[2], 0) +1

        #Total votes calculation    
        total_votes = len(vote_ids)  

        print("Total Votes: " + str(total_votes))
        print("-------------------------")

        #Calculating list of cadicates and percentage of votes they got
        for k, v in candidates.items():
            percentage = round(((v/total_votes)*100), 3)
            print (k + ": " + str(percentage) + "% (" + str(v) + ")") 

        # Calculating winner
        winner = max(candidates, key=candidates.get)
        print("-------------------------")
        print("Winner: " + winner)  
        print("-------------------------")
      
    #main function
    def main():
        vote_analyze() 

    if __name__=="__main__":
        main()      