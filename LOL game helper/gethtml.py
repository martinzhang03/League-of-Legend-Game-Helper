from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get("http://op.gg/statistics/champions?region=kr")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

def opggtohtml():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://op.gg/statistics/champions?region=na")
    elem = driver.find_element("id", "__next")
    source_code = elem.get_attribute("innerHTML")
# text_file = open('getcode', 'w')
    with open("fromopgg.html", "w") as html_file:
        html_file.write(source_code)

# parsed_html = BeautifulSoup(source_code)
# print(type(parsed_html))
#text_file.write(parsed_html)
# print(parsed_html)
# elem = driver.find_element_by_class_name("css-1hhfha5 e1thjuil1")
# print(elem)

# import requests
#
#
# url = 'http://op.gg/statistics/champions?region=kr'
# headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}
# r = requests.get(url, headers=headers,allow_redirects=True)
#
# open('getcode', 'wb').write(r.content)