import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "google.com"

with open("subdomain-wordlist.txt", "r") as wordlist:
    for line in wordlist:
        stripped_line = line.strip()
        test_url = stripped_line + "." + target_url
        resp = request(test_url)
        if resp:
            print("[+] discovered subdomain ---> " + test_url)
