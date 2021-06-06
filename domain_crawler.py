import requests
from bs4 import BeautifulSoup

all_domain = []


def extract_domains():
    resp = requests.post(url="https://domainbigdata.com/nj/2yTlQHiod9ZJe-gXgtJ_9A")
    y = BeautifulSoup(resp.content, "lxml")
    t = y.find("table", attrs={"class": "t1"})
    z = t.find("tbody")
    for k in z.findAll("tr"):
        for p in k.findAll("td")[0]:
            all_domain.append(p.text)


extract_domains()
for domain in all_domain:
    print(domain)
