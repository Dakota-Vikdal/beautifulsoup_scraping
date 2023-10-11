from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
subtext = soup.select('.subtext')

# Grab the title, link and vote of each hacker news article with 100 votes or more.
def my_hacker_news(links, subtext):
    # Create a list you can append high voted articles to.
    hacker_news = []
    # Iterate over links, titles and votes to isolate the ones you want.
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            votes_text = int(vote[0].getText().replace(' points', ''))
            if votes_text > 100:
                hacker_news.append({'title': title, 'link': href})
            
    return hacker_news 
print(my_hacker_news(links, subtext))