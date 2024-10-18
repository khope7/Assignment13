#Task 1: Email Extraction Enhancement
# 
# Problem Statement: You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). Modify the script to extract all email addresses except those from the specified domain.
#
#Code Example:
#
#import re
#
#text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
#emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
#print(emails)

#Writing code for PythonRegExpressionsDeepDiveTask1


#Instantiating Regular Expressions
import re

#Instantiating example text
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

#Instantiating example regex
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

#Creating Welcome message
print("Printing all domains that exclude 'exclude.com':")
      
#Emails prints as list, using for loop to print list out as a string excluding all 'exclude.com' domains
for domain in emails:
    if "exclude.com" not in domain:
        print(f"{domain}")

#Adjusting findall method to only include domain.com and printing alternate method
alt_method = re.findall(r"\b[A-Za-z0-9._%+-]+@[domain.com]+\.[A-Z|a-z]{2,}\b", text)

print(f"\nModifying regex method to show for only domains with 'domain.com' domains:\n{alt_method}")

#NOTE: Not sure how to exclude full words using regex methods