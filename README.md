# **Web Parsing www.organcity.com**

### **Project Description**
This script scrapes product information from the website www.organcity.com and saves it into a CSV file named organs1.csv. The script iterates through different product categories and extracts details such as product names, ratings, and prices.

### **Features**
The script performs the following tasks:

• Constructs the URL for each product category.

• Makes a GET request to the URL and retrieves the HTML content.

• Parses the HTML content using BeautifulSoup.

• Finds the section containing product information.

• Keeps track of the current page number.

• Adds a random delay between requests to avoid overloading the server.

• Extracts and writes the main header (Latest, Best Selling), sub-headers (Product, Rating, Price), and product details to the CSV file.

### **Required Libraries**
•	requests

•	beautifulsoup4

•	(csv, time, random)
