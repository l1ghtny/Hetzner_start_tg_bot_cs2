import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# URL = "https://www.hltv.org/results?stars=3"
#
# referer = f'https://hltv.org/results'
# headers = {
#             'User-Agent': (
#                 'Mozilla/5.0 '
#                 '(iPhone; CPU iPhone OS 13_2_3 like Mac OS X) '
#                 'AppleWebKit/605.1.15 (KHTML, like Gecko) '
#                 'Version/13.0.3 Mobile/15E148 Safari/604.1'
#             ),
#             'Referer': referer
#         }
#
#
# page = requests.get(URL, headers=headers)
#
#
# soup = BeautifulSoup(page.content, "html.parser")
#
# result_table = soup.find('div', class_='results-holder allres')
# results = result_table.find_all('div', class_='result-con')

# for i in results:
#     links = i.find_all("a")
#     for link in links:
#         link_url = link["href"]
#         print(link_url)
#         result = i.find('div', class_='result')
#         team1 = result.find('div', class_='line-align team1')
#         team2 = result.find('div', class_='line-align team2')
#         score_won = result.find('span', class_='score-won')
#         score_lost = result.find('span', class_='score-lost')
#         if team1.find('div', class_='team team-won') is not None:
#             team1_won = True
#         else:
#             team1_won = False
#         if team1_won:
#             print('won: ', team1.text)
#         else:
#             print('won: ', team2.text)
#         options = Options()
#         options.add_argument("--headless")
#         driver = webdriver.Firefox(options=options)
#         driver.get(f"https://www.hltv.org/{link_url}")
#         soup2 = BeautifulSoup(driver.page_source, 'html.parser')
#         event = soup2.find('div', class_='event text-ellipsis')
#         print('event: ', event.text)
#         event_link = event.find('a')
#         print(event_link['href'], '\n')
#         driver.stop_client()


async def get_results(star: int, de_map: str):
    URL = f"https://www.hltv.org/results?stars={star}&map=de_{de_map}"

    referer = f'https://hltv.org/results'
    headers = {
        'User-Agent': (
            'Mozilla/5.0 '
            '(iPhone; CPU iPhone OS 13_2_3 like Mac OS X) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) '
            'Version/13.0.3 Mobile/15E148 Safari/604.1'
        ),
        'Referer': referer
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    result_table = soup.find('div', class_='results-holder allres')
    results = result_table.find_all('div', class_='result-con')
    buttons = []
    for i in results:
        links = i.find_all('a')
        for link in links:
            result = link.find('div', class_='result')
            team1 = link.find('div', class_='line-align team1')
            team2 = result.find('div', class_='line-align team2')
            score_won = result.find('span', class_='score-won')
            score_lost = result.find('span', class_='score-lost')
            if team1.find('div', class_='team team-won') is not None:
                team1_won = True
            else:
                team1_won = False
            if team1_won:
                button_text = f'{team1.text} {score_won.text}:{score_lost.text} {team2.text}'
            else:
                button_text = f'{team2.text} {score_won.text}:{score_lost.text} {team1.text}'
            buttons.append(button_text)
    return buttons

