from bs4 import BeautifulSoup

def gettopfive():
    with open('fromopgg.html', 'r') as file:
        content = file.read()
    soup = BeautifulSoup(content, 'lxml')
    tags = soup.find_all('tr', class_ = 'top')
    library = []
    for every in tags:
        heroname = every.find_all('a')
        # print(heroname)
        winrate = every.find('span', class_ = 'value')
        gold = every.find('span', class_ = 'value orange')
        KDA = every.find('span', class_ = 'ratio')
        individual = {'name': 'empty', 'winrate': 0.00, 'gold': 0, 'kda': 0.00}
        for it in heroname:
            a = it.text
            a = a.strip()
            if a:
                individual['name'] = a
                individual['winrate'] = winrate.text
                individual['gold'] = gold.text
                individual['kda'] = KDA.text
            # list_stats = set([])
            # for toit in stat:
            #     list_stats.add(toit.text)
            #     # print('stats: \n', toit.text)
            #     individual['stats'] = list_stats

            if not individual['name']=='empty':
                library.append(individual)
    return library
    # print(library)