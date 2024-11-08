#!./my-venv/bin/python3
# WikipediaPythonLink.py
# Utiliza do selenium para abrir o Chrome, no artigo do Linux no Wikipedia e entra em todos os links
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

#service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("https://pt.wikipedia.org/wiki/Linux")

self.assertIn("Linux – Wikipédia, a enciclopédia livre",
               driver.title)

links = driver.find_elements_by_tag_name("a")
for link in links:
    url = link.get_attribute("href");
    driver.get(url)
    print(url);
    
driver.close()

