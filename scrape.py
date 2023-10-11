from bs4 import BeautifulSoup
import requests
import pprint

    
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/?p=2')
res3 = requests.get('https://news.ycombinator.com/?p=3')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
soup3 = BeautifulSoup(res3.text, 'html.parser')
links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')
links3 = soup3.select('.titleline > a')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
subtext3 = soup3.select('.subtext')

mega_links = links + links2 + links3
mega_subtext = subtext + subtext2 + subtext3

def highest_to_lowest(input_list):
    ranked_list = sorted(input_list, key=lambda k: k['votes'], reverse = True)
    return ranked_list

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
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hacker_news.append({'title': title, 'link': href, 'votes': points})
            
    return highest_to_lowest(hacker_news) 
pprint.pprint(my_hacker_news(mega_links, mega_subtext))