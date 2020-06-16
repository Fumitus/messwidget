import os
import requests
import re


def request(url):
    r = requests.get(url)
    return r


def filter_r(r_text, text):
    stripped = re.search('<li>(.*?)</li>', r_text)
    if text == stripped:
        print(text)
    else:
        print("No new mwsages")


def main(passed_args=None):

    url = 'http://127.0.0.1:5000/index'
    r = request(url)
    r_text = r.text
    text = 'įrasas paskelbtas'
    filter_r(r_text, text)


if __name__ == "__main__":
    main()


