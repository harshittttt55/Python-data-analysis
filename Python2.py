#Extracting Data from XML

import urllib.request
import xml.etree.ElementTree as ET

def main():
    # Prompt the user for the URL
    url = input("Enter location: ")

    # Retrieve and read the XML data from the URL
    print(f"Retrieving {url}")
    response = urllib.request.urlopen(url)
    data = response.read()

    # Print the size of the retrieved data
    print(f"Retrieved {len(data)} characters")

    # Parse the XML data
    tree = ET.fromstring(data)

    # Use XPath to find all 'count' elements
    counts = tree.findall('.//count')

    # Calculate the sum of the counts
    total_sum = sum(int(count.text) for count in counts)

    # Print the count of 'count' elements and their sum
    print(f"Count: {len(counts)}")
    print(f"Sum: {total_sum}")

if __name__ == "__main__":
    main()