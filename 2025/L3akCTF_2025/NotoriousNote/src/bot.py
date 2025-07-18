from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 

class Bot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox") 
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-extensions") 
        chrome_options.add_argument("--window-size=1920x1080") 
        
        self.driver = webdriver.Chrome(options=chrome_options)

    def visit(self, url):
        self.driver.get("http://127.0.0.1:5000/")
        
        self.driver.add_cookie({
            "name": "flag", 
            "value": "L3AK{fake_flag}", 
            "httponly": False  
        }) 
        
        self.driver.get(url)
        time.sleep(1)
        self.driver.refresh()
        print(f"Visited {url}")

    def close(self):
        self.driver.quit()