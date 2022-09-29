from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup

def getcode():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    path = "https://na.op.gg/summoners/na/"
    name = input()
    path = path+name
    driver.get(path)
    bt = driver.find_element("class name","action")
    bt.click()
    elem = driver.find_element("id", "__next")
    source_code = elem.get_attribute("innerHTML")
# text_file = open('getcode', 'w')
    with open("gamerecord.html", "w") as html_file:
        html_file.write(source_code)



