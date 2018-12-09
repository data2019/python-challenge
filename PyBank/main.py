import os
import csv

#Read .csv file and skip header
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #declearing lists to store both columns of .csv file
    months = []
    net_amount = []
    
    # method to calculate Total Months, Total profit/losses, avareage change, greatest increase in profits, greatest decrease in losses
    def financial_analysis():

        #declearing variables to store values
        prev_value = 0
        change = 0
        greatest_increase = 0
        increase_date = 0
        greatest_decrease = 0
        decrease_date = 0

        # for loop to loop through .csv file rows
        for row in csvreader:
            months.append(row[0])
            
            #casting profit/losses to float
            amount_cast = float(row[1])
            net_amount.append(amount_cast)

            #greatest increase in profits, greatest decrese in losses calculation
            change = amount_cast - prev_value
            prev_value =amount_cast
            if change > greatest_increase:
                greatest_increase = change
                increase_date = row[0]
            if change < greatest_decrease: 
                greatest_decrease = change
                decrease_date = row[0]    

        #Total number of months
        num_month = len(months)
        #Total net amount
        total = sum(net_amount)
        #Average change calculation
        amount_diff = (net_amount[len(net_amount)-1] - net_amount[0])
        avg_change = amount_diff/(len(months)-1)
        avg_change = round(avg_change, 2)

        #Print output
        print("Financial Analysis")
        print("----------------------------")
        print("Total Months: "+ str(num_month))
        print("Total: " + "$" + str(total))
        print("Average  Change: " + "$" +str(avg_change))
        print("Greatest Increase in Profits: " + increase_date + " (" + str(greatest_increase) + ")")
        print("Greatest Decrease in Profits: " + decrease_date + " (" + str(greatest_decrease)+ ")")

    #main function
    def main():
        financial_analysis() 

    if __name__=="__main__":
        main()    