import requests
import re
import urlparse

target_url = "https://domainbigdata.com/"
target_links = []


def extract_links(url):
    resp = requests.get(url)
    return re.findall('(?:href=")(.*?)"', resp.content)

href_links = extract_links(target_url)

for link in href_links:
    link = urlparse.urljoin(target_url, link)

    if "#" in link:
        link = link.split("#")[0]

    if target_url in link and link not in target_links:
        target_links.append(link)
        print(link)