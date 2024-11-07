from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

#service = Service(ChromeDriverManager().install())
class WikipediaPythonLink():
    def setUp(self):
        self.driver = webdriver.Chrome()

    
    def clica_link_wikipedia(self):
        driver = self.driver
        driver.get("https://pt.wikipedia.org/wiki/Linux")

        self.assertIn("Linux – Wikipédia, a enciclopédia livre",
                       driver.title)

        search_box = driver.find_element(by=By.NAME, value="q")
        search_box.clear()
        search_box.send_keys("pycon")
        search_box.send_keys(Keys.RETURN)
        self.assertIn("No results found.", driver.page_source)
    
   

    def fechaFirefox(self):
        self.driver.close()
    