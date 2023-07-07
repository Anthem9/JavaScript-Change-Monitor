import json
import requests
from bs4 import BeautifulSoup
import time
import difflib
from urllib.parse import urljoin


class JSChangeMonitor:
    def __init__(self, config):
        self.url = config["url"]
        self.check_interval = config["check_interval"]
        self.xizhi_key = config["xizhi_key"]
        self.current_js_content = self.get_js_content(self.url)

    def get_js_content(self, url):
        """
        获取给定url页面中所有JavaScript的内容

        :param url: 需要获取JavaScript的页面url
        :return: 一个字典，键为脚本url或页面url，值为JavaScript内容的列表
        """
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        js_codes = {}
        for script in soup.find_all('script'):
            if script.get('src'):
                try:
                    # Make sure to handle relative URLs
                    src_url = urljoin(url, script.get('src'))
                    r = requests.get(src_url)
                    if r.status_code == 200:
                        js_codes[src_url] = r.text.split('\n')
                        js_codes.update(self.get_js_content(src_url))
                except:
                    pass
            else:
                js_codes[url] = (script.string if script.string else '').split('\n')

        return js_codes

    def monitor(self):
        """
        开始监视JavaScript的变化
        """
        while True:
            new_js_content = self.get_js_content(self.url)
            for url, new_content in new_js_content.items():
                if url not in self.current_js_content or new_content != self.current_js_content[url]:
                    print(f"JavaScript code changed in {url} at {time.ctime()}")
                    if url in self.current_js_content:
                        diff = difflib.unified_diff(self.current_js_content[url], new_content)
                        diff_content = '\n'.join(diff)
                        print(diff_content)
                        self.current_js_content = new_js_content
                        requests.post(url=self.xizhi_key,
                                      params={"title": "JS changed",
                                              "content": diff_content})
                else:
                    print(f"JavaScript code didn't change at {time.ctime()}")
                requests.post(url=self.xizhi_key,
                             params={"title": "JS didn't change",
                                     "content": "Nothing"})
                time.sleep(self.check_interval)


with open("config.json", "r") as file:
    config = json.load(file)

monitor = JSChangeMonitor(config)
monitor.monitor()
