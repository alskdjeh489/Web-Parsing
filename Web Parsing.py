# Web Parsing www.organcity.com

# Required libraries
import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint


# Creating CSV file
file = open('organs1.csv', 'w', newline='\n')
write_obj = csv.writer(file)

# Data
# Instead of numbers the website uses the following words for paging
products = ['human-kidney', 'human-heart', 'human-lungs', 'human-liver']
page = 1  # Used to keep track of the current page number in the file.

# Looping through pages
for product in products:
    url = f'https://organcity.com/product-category/{product}/'
    response = requests.get(url)
    content = response.text

    write_obj.writerow([f'Page {page}'])

    soup = BeautifulSoup(content, 'html.parser')
    section = soup.find('div', class_='footer-widgets')
    categories = section.find_all('div', class_='widget_products')
    # print(sections)
    # print(categories)

    for category in categories:
        title = category.find('span', class_='widget-title').text.strip()  # Headers for rows
        # print(title)  # Result: 'Latest'; 'Best Selling'

        write_obj.writerow([title])
        write_obj.writerow(['Product', 'Rating', 'Price'])  # Sub-headers

        listing = category.find_all('li')
        for item in listing:
            name = item.find('span', class_='product-title').text.replace('For Sale', '').strip()
            price = item.bdi.text.strip()
            if item.find('strong') is not None:
                rating = item.strong.text.strip()
            else:
                rating = 'Not Rated'

            write_obj.writerow([name, rating, price])

        write_obj.writerow([''])  # Adding space between the rows

    page += 1

    time.sleep(randint(15, 20))  # Defining time duration of sending requests to the server

file.close()
