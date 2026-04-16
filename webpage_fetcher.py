import time
import requests
import logging

logging.basicConfig(filename="log.log",filemode="a", format="%(asctime)s - %(message)s")

class WebHandler:
    def __init__(self,main_url,user_agent_name,user_agent_email,max_rabbit_hole=6):
        self.main_url = main_url
        self.max_rabbit_hole = max_rabbit_hole
        self.user_agent_name = user_agent_name
        self.user_agent_email = user_agent_email
        self.headers = {
                'User-Agent': f'{user_agent_name}/1.0 (f{user_agent_email})'
        }

    def fetch(self,topic_name):
        time.sleep(5)
        request_url = self.main_url+"/"+topic_name
        assert request_url=="https://en.wikipedia.org/wiki/Cairo"
        try:
            response = requests.get(request_url,headers=self.headers)
            print("response is",response)
            assert response.status_code == 200
            if response.status_code==200:
                response.encoding = 'utf-8'
                return response.text
            else:
                return None
        except:
            logging.exception(f"Error Occurred while fetching webpage topic {topic_name}")
            return None