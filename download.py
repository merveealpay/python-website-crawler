import requests


def download(url):
    resp = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(resp.content)


download("asddsd")
