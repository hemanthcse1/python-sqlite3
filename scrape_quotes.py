import requests
from bs4 import BeautifulSoup
import csv

with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author', 'Tags'])


    base_url = "http://quotes.toscrape.com"
    next_page = "/page/1/"

    while next_page:
        url = base_url + next_page
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all("div", class_="quote")
        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
            writer.writerow([text, author, ', '.join(tags)])


        next_button = soup.find("li", class_="next")
        if next_button:
            next_page = next_button.find("a")["href"]
        else:
            next_page = None

print("✅ All quotes scraped and saved to quotes.csv!")
