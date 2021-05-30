import requests


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


target_url = ""

with open("files-and-dirs-wordlist.txt", "r") as wordlist:
    for line in wordlist:
        stripped_line = line.strip()
        test_url = target_url + "/" + stripped_line
        resp = request(test_url)
        if resp:
            print("[+] discovered URL ---> " + test_url)
