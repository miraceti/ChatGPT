import requests
from bs4 import BeautifulSoup

url = "https://www.nasa.gov/mission_pages/juno/main/index.html"
page = requests.get(url)
html_content = page.content
soup = BeautifulSoup(html_content, "html.parser")
print(soup)
#title = soup.find("h1").text
#print(title)

# title_element = soup.find("h1")
# if title_element:
#     title = title_element.text
# else:
#     title = "Titre non trouvé"

links = soup.find_all("link")
print(links)
for link in links:
    print(link.text, link["href"])

# link_elements = soup.find_all("a")
# if link_elements:
#     for link in link_elements:
#         print(link.text, link["href"])
# else:
#     print("Aucun lien trouvé")