import requests
import re


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = "domainbigdata.com"

resp = request(target_url)

href_links = re.findall('(?:href=")(.*?)"', resp.content)

print(href_links)
