import urllib.request
from bs4 import BeautifulSoup


def scrape_numbers_from_url(url):
    # Step 1: Retrieve the HTML from the URL
    print(f"Retrieving data from: {url}")

    try:
        response = urllib.request.urlopen(url)
        html = response.read()
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return
    # Step 2: Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Step 3: Find all <span> tags with the class "comments"
    span_tags = soup.find_all('span', class_='comments')

    # Step 4: Extract numbers and calculate the sum
    total_sum = 0
    for span in span_tags:
        # Extract the text, convert to integer and add to the total sum
        number = int(span.text)
        total_sum += number

    # Step 5: Output the result
    print(f"The total sum of the numbers is: {total_sum}")


# Input URL for the assignment
url = 'http://py4e-data.dr-chuck.net/comments_2129134.html'  # Replace with your actual data URL
scrape_numbers_from_url(url)
