import requests


def request(url):
    try:
        #requests.request("GET")
        return requests.get("http://" + url)
    except requests.exceptions.HTTPError:
        pass

target_url = "google.com"

with open("subdomain-wordlist.txt", "r") as wordlist:
    for line in wordlist:
        stripped_line = line.strip()
        test_url = f"{stripped_line}.{target_url}"
        #test_url = stripped_line + "." + target_url
        if request(test_url):
            print("[+] discovered subdomain ---> " + test_url)
