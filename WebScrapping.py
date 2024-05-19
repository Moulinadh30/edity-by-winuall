# Install necessary libraries if not already installed
# !pip3 install requests
# !pip3 install beautifulsoup4
# !pip3 install pandas

import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for i in range(1, 5):
    # Define the URL with page number
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    
    # Send a GET request to the website
    response = requests.get(url)
    response = response.content
    
    # Parse the HTML content
    soup = BeautifulSoup(response, 'html.parser')
    
    # Find the <ol> tag containing book information
    ol = soup.find('ol')
    
    # Find all <article> tags with class 'product_pod'
    articles = ol.find_all('article', class_='product_pod')
    
    # Iterate through each article to extract book details
    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        starTag = article.find('p')
        star = starTag['class'][1]
        price = article.find('p', class_='price_color').text
        price = float(price[1:])
        books.append([title, star, price])

# Create a DataFrame from the collected data
df = pd.DataFrame(books, columns=['Title', 'Star Rating', 'Price'])

# Save DataFrame to a CSV file
df.to_csv('books.csv', index=False)
