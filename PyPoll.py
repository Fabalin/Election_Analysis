# Import relevant modules for analysis- CSV file reading and indirect path file access
import csv
import os 

# Add file name variable that references the file's path indirectly using chaining
file_to_load = os.path.join("Resources", "election_results.csv")

# Open file using file name variable using WITH statement as file name obj
with open(file_to_load) as election_data:

    #Read the file object with the reader function. 
    file_reader = csv.reader(election_data)

    #Skip the first row of the column headers using next() and print to confirm
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file. 
    for row in file_reader:
        print(row)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the with statement to open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write some data to the file 
    txt_file.write("Counties in the Election")
    txt_file.write("\n-----------------------------------")
    txt_file.write("\nArapahoe\nDenver\nJefferson")
