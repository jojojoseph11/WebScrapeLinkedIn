import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/search/results/people/?currentCompany=%5B%221441%22%5D&geoUrn=%5B%22103644278%22%5D&heroEntityKey=urn%3Ali%3Aorganization%3A1441&keywords=google&origin=FACETED_SEARCH&position=0&searchId=305992b4-1583-4c1d-a03f-38b80c605216&sid=Ut.'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find_all()

print("hello, world!",results)

for result in results:
    title = result.find('span', {'class': 'a-size-medium'})
    price = result.find('span', {'class': 'a-offscreen'})
    rating = result.find('span', {'class': 'a-icon-alt'})
    if title and price and rating:
        print('Title:', title.text)
        print('Price:', price.text)
        print('Rating:', rating.text)
        print('------------------------')