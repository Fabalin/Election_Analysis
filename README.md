# Election_Analysis
Analyzing Election Poll Data Using Python

## Project Overview 
A Colorado Board of Elections employee had asked to analyze the polling data of a local congressional election. Python programming language was used to read the poll results contained within a csv file. The output of the analysis was summarized in a text file following the criteria specified below:

  1. The total number of votes cast. 
  2. A List of candidates who recieved votes. 
  3. Calculate each candidate's total number of votes. 
  4. Calculate the each candidate's percentage of votes recieved.
  5. Determine the winner of the election based on popular vote count.  

### Challenge Overview 
The challenge used the desgin pattern of the project to perform a similar analysis and determine the county with the largest voter turnout. The criteria to be displayed in the text file includes:

  1. A list of counties where votes were cast.
  2. The total number of votes cast by each county. 
  3. The percentage of votes cast by each county. 
  4. Determine the county with the largest turnout based on popular vote. 

## Resources
- Data Source: [election_results.csv](https://github.com/Fabalin/Election_Analysis/blob/main/Resources/election_results.csv)
- Results of Analysis: [election_results.txt](https://github.com/Fabalin/Election_Analysis/blob/main/analysis/election_results.txt)
- Software: Python 3.6.1, Visual Studio Code, 1.64.2 
- Code: [Pypoll_Challenge.py](https://github.com/Fabalin/Election_Analysis/blob/main/PyPoll_Challenge.py)

## Election-Audit Results  
![Election Results Python Analysis Output As Text File](https://github.com/Fabalin/Election_Analysis/blob/main/analysis/election_results.PNG)

- Based on the output file above, the total congressional votes cast for this election was **369,711**.  

- There were 3 counties that participated in this election: Jefferson, Denver, and Arapahoe. 
  - **Jefferson** recieved a total of 38,855 votes, resulting in 10.5% of the total votes.  
  - **Denver** recieved a total of 306,055 votes, resulting in 82.8% of the total votes.
  - **Arapahoe** recieved a total of 24,801 votes, resulting in 6.7% of the total votes.  
 
- **Denver** had the largest turnout among the counties.

- There were 3 candidates that recieved votes in this election: Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane. 
  - **Charles Casper Stockham** recieved a total of 85,213 votes, resulting in 23% of the total votes.  
  - **Diana DeGette** recieved a total of 272,892 votes, resulting in 73.8% of the total votes.
  - **Raymon Anthony Doane** recieved a total of 11,606 votes, resulting in 3.1% of the total votes. 
 
- Based on the popular vote, the winning candidate was **Diana DeGette** who recieved a total of **272,892 votes** representing **73.8%** of the total votes.

## Election-Audit Summary 
The [Pypoll_Challenge](https://github.com/Fabalin/Election_Analysis/blob/main/PyPoll_Challenge.py) code can be modified to perform the election analysis for any election across different operating systems since it contains the `os` module. Two examples of modifications are idenfified as below:   

- The first modification must focus on specifying the path to the data file to be analyed as well as the folder for the output file in **lines 9 and 11**. 
  ```
  8   # Add a variable to load a file from a path.
  9   file_to_load = os.path.join("Resources", "election_results.csv")
  10  # Add a variable to save the file to a path.
  11  file_to_save = os.path.join("analysis", "election_results.txt")
  ```
  The written code uses the `os.path.join` function to identify the relative path of the data file and the output file. Modify the code by identifying the relative path of the data file and the output file. Input the paths into the `os.path.join` function with each level of the relative path written between quotation marks and commas separating each element in the path. By default, the output file will be generated automatically as a text file since line 35 of the code includes the `open()` function in the`"w"` mode: 
  ```
  34  # Save the results to our text file.
  35  with open(file_to_save, "w") as txt_file:
  ```
  If the file with the name does not exist, the program will create the file. **Rename** the output file accordingly by modifying the `"election_results.txt"` in **line 11** if the file name is already taken as the program output will overwrite over the existing file. 
  
- The second modification will focus on modifying the code to suit csv data files with a different layout of the data. The current code assumes that the name of the candidiate is in the third column of the CSV file and the county name is in the second column. However, other elections might collect additional data fields such as time stamps. In cases where the csv file layout is different, modify the index values in **lines 48 and 51** accordingly to reflect the columns containing the apporpriate data fields specified. 
  ```
  34  # Read the csv and convert it into a list of dictionaries
  35  with open(file_to_load) as election_data:
  36      reader = csv.reader(election_data)
  ...
  47          # Get the candidate name from each row.
  48          candidate_name = row[2]
  49  
  50          # 3: Extract the county name from each row.
  51          county_name = row[1]
  ```
  The `csv.reader()` function reads each row of the CSV file as a list with the columns being the elements of the list. As such proper indexing is required to collect the correct element of the list containing the desired data. 
