#Extracting Data With Regular Expressions
import re
import urllib.request

# Prompt the user to enter the URL
url = input("Enter the URL: ")

try:
    # Fetch the data from the URL
    response = urllib.request.urlopen(url)
    # Read the response and decode it to get the content as a string
    data = response.read().decode()

    # Initialize a variable to hold the sum of the numbers
    total_sum = 0

    # Process the data line by line
    for line in data.splitlines():
        # Use re.findall to find all the numbers in the line
        numbers = re.findall('[0-9]+', line)

        # Convert the numbers from strings to integers and add them to the total sum
        total_sum += sum(int(number) for number in numbers)

    # Print the total sum of the numbers found
    print(f"The sum of the numbers in the file is: {total_sum}")

except Exception as e:
    print(f"Error: {e}")
