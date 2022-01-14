# Python_challenge_1

## Overview

The Colorado Board Of Elections needs to tally the vote from a recent Congressional election.  They have the results of the election stored as a .csv file, containing each voter's voter ID number, county of residence, and choice of candidate.  Using python, we have automated the process of the vote tally.

## Results

The results of the analysis performed on the election data are as follows:

* Total votes: **369,711**
* Jefferson County had **38,855** votes, for **10.50%** of the total
* Denver County had **306,055** votes, for **82.78%** of the total
* Araphoe County had **24,801** votes, for **6.71%** of the total
* Denver County had the highest turnout
 
 
* Charles Casper Stockham recieved **23.05%** of the vote (**85,213** total)
* Diana DeGette recieved **73.81%** of the vote (**272,892** total)
* Raymon Anthony Doane recieved **3.14%** of the vote (**11,606** total)
 
 
* Diana Degette won the election, with **73.81%** of the vote (**272,892** total)

## Summary

This script is great for handling a single election, however, the file names are hard coded, so it could become cumbersome to use to count elections for multiple districts at once.  With some modifications, the script could be used to tally any number of elections, so long as the data is in the same format.

The following line of code will assemble a list of strings containing the file path and name of all files within a directory called 'resources', and could be used to iterate across each file accordingly.  However, this modification will require results to be saved as .csv files, named `<countyName>.csv`.

```
# assemble a list of paths to files within the resources directory
filenames = [os.path.join('resources', filename) for filename in os.listdir('resources')]

for file in filenames:
  # find the file name (any characters preceded by "\" and followed by ".csv"), then insert it into a valid output filepath
  outputfile = os.path.join('analysis', re.search("(?<=\\\\).*(?=\.csv)", filenames[0]).group()) + '_results.txt'
  # perform analysis and write to file
```

Additionally, safeguards could be added to remove duplicate rows in the input .csv:

```
voterIDs = []

for inputFile in filenames:
 with open(inputFile) as election_data:
    reader = csv.reader(election_data)
    header = next.reader
    for row in reader:
     voterID = reader[0]
     if voterID not in voterIDs:
       voterIDs.append(voterID)
       # perform the rest of the tally
```

This could be used to make sure that the resulting tally is correct, regardless of any duplicate entries in the input data.



