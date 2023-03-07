# coding: utf-8

import time
from selenium import webdriver
from pathlib import Path

__author__ = "Jaejin Jang<jaejin0me@gmail.com>"

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
    options.add_argument("lang=ko_KR")
    webdriverpath = Path.joinpath(Path.cwd(), "driver", "chromedriver")
    print(webdriverpath)

    driver = webdriver.Chrome(webdriverpath, options=options)
    time.sleep(1)

    driver.close()
