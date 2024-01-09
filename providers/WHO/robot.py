from bs4 import BeautifulSoup
import requests
import re

# Example
url = 'https://www.cdc.gov/niosh/index.htm'
search_for = 'COVID'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    covid_links = soup.find_all('a', href=True)
    filtered_links = (l for l in covid_links if search_for in l.get_text())

    for link in filtered_links:
        link_url = link['href']
        print(f"URL do Link: {link_url}\n")
else:
    print("Falha ao obter a página:", response.status_code)


# Searching page
# url = 'https://www.who.int/home/search?indexCatalogue=genericsearchindex1&searchQuery=coronavirus&wordsMode=AnyWord'
# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = soup.find_all('a')
#     for link in links:
#         link_url = link['src']
#         print(f"URL do Link: {link_url}\n")
# else:
#     print("Falha ao obter a página:", response.status_code)


