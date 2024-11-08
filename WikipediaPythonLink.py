#!./my-venv/bin/python3
# WikipediaPythonLink.py
# Utiliza do selenium para abrir o Chrome, no artigo do Linux no Wikipedia e entra em todos os links
# TO-DO: Para abrir navegador no terminal abrir em SANDBOX
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By;
from selenium.webdriver.common.action_chains import ActionChains;
import time;
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

#service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome();
driver.get("https://pt.wikipedia.org/wiki/Linux");

assert("Linux – Wikipédia, a enciclopédia livre" in driver.title);

links = ['Linux (desambiguação)', 'sistemas operacionais', 'kernel', 'Linus Torvalds'];

for link in links:
    url =driver.find_element(By.LINK_TEXT, link).click();
    time.sleep(5);
    driver.close();

    

