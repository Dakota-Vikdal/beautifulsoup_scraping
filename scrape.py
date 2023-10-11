from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
votes = soup.select('.score')

# Grab the title, link and vote of each hacker news article with 100 votes or more.
def my_hacker_news(links, votes):
    # Create a list you can append high voted articles to.
    hacker_news = []
    # Iterate over links and votes to isolate the ones you want.
    # Use enumerate here in order to keep the titles, links, and votes
    # of each article together.
    for index, items in enumerate(links):
        if links and votes == True:
            title = links[index].getText()
            href = links[index].get('href')
            print(title)
            votes_text = int(votes[index].getText().replace(' points', ''))
            if votes_text > 100:
                print(hacker_news.append({'title': title, 'link': href}))
            
    return hacker_news 
print(my_hacker_news(links, votes))

# for link in links:
#     link_tag = link.find('a')
#     grab_link = link_tag['href']
#     print(grab_link)
#     # Iterate over links in order to breakdown the list into individual elements.
#     for vote in votes:
#         # Access the score within each link.
#         score_text = vote.getText()
#         score_num = int(score_text.split()[0])
#         # Remove all links that have a score under 100
#         if score_num >= 100:
#             print(score_num)
#             print(grab_link)