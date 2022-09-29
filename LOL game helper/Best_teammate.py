from interact import *
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

getcode()
with open("gamerecord.html", 'r') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('div', class_ = 'text')
    winrate = tags[-1].text
    print(winrate)
    players = []
    out = soup.find('div', class_ = 'css-1sq1kbv e1shm8tx0')
    target = out.find_all('td', class_ = 'name')
    for it in target:
        players.append(it.text)
    players_path = []
    for each in players:
        each = each.replace(" ", "")
        text = "https://na.op.gg/summoners/na/"
        text = text+each
        players_path.append(text)
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    for it in players_path:
        driver.get(it)
        elem = driver.find_element("id", "__next")
        source_code = elem.get_attribute("innerHTML")
        soup = BeautifulSoup(source_code, 'lxml')
        tags = soup.find_all('div', class_ = 'text')
        winrate = tags[-1].text
        print(winrate)