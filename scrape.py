from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.score')

score = []
# Iterate over links in order to breakdown the list into individual elements.
for link in links:
    # Access the score within each link.
    score_text = link.getText()
    score_num = int(score_text.split()[0])
    # Remove all links that have a score under 100
    if score_num >= 100:
        score_num