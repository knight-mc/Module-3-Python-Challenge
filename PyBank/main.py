import os
import csv

rowcount = -1      #start at -1 to account for header
totalrev = 0
averageChange = 0
holdChange =0
holdprevious = 0
i = 1

Month = []
Revenue = []
change = []

csvpath =  os.path.join("resources", "budget_data.csv")
#print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        rowcount += 1
        if rowcount > 0:
            Month.append(row[0])
            Revenue.append(row[1])
            totalrev = int(totalrev) + int(row[1])

    ###############   
    while i < (rowcount):
        holdprevious= int(Revenue[(i-1)])
        holdchange = int(Revenue[i]) - holdprevious
        change.append(holdChange)

        # python does not execute with this function added
    ################    
    print(rowcount)
    print(totalrev)

  
    

    #count number of months (find unique)
    #net total of profit and losses, sum
    #new series for difference between months(rows)
    #average of those changes
    #greatest value in the new series for greatest increase
    #lowest value in the new series for greatest decrease

    #Print analysis with results
    #Create text file with results