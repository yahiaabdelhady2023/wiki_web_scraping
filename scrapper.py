import time
from bs4 import BeautifulSoup
import logging


logging.basicConfig(filename="log.log",filemode="a", format="%(asctime)s - %(message)s")





class Scrapper:
    def parse_html(self,html_text):
        print("html_text is",html_text)
        try:
            soup=BeautifulSoup(html_text,"html.parser")
            return soup
        except:
            logging.exception(f"Error to parse html_text")
            return None