# Task 03 – Email Extractor Script
**Student:** bharat singh chouhan  
**Student ID:** CA/DE1/1099  
**Domain:** Python Programming  

## Project Description
This Python script reads text from an input file, extracts all valid email addresses using a refined regular expression, removes duplicates, and saves the results to a clean output file.  
The goal of this task is to automate a common text-processing requirement that appears in data cleaning and document scanning workflows.

## Features
- Reads text from a .txt file  
- Extracts email addresses using an advanced regex pattern  
- Removes duplicate email entries  
- Sorts results alphabetically  
- Saves unique emails to a new .txt file  
- Includes error handling and clean console messages  

## Tech Used
- Python  
- Regex (re module)  
- File handling  



---------------------------------------------------------------------------------------------

## How to Run
1. Place your text inside `input.txt`
2. Run the script:

>Email_Extractor.py 

3. Extracted emails will be saved to:
extracted_unique_emails.txt

## Example

**input.txt**
Hello, contact us at support@example.com
or mail the team at info@service.in and HELLO123@company.org.

markdown
Copy code

**extracted_unique_emails.txt**
hello123@company.org
info@service.in
support@example.com

markdown
Copy code

## Notes
- The script handles uppercase and lowercase email variations.  
- All extracted emails are converted to lowercase for consistent output.  
- Advanced email matching helps detect common patterns including subdomains.







