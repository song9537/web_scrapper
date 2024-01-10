from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import csv
import time


def extract_wanted_jobs(keyword):

    p = sync_playwright().start()

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

    for x in range(5):
        time.sleep(0.5)
        page.keyboard.down("End")

    content = page.content()

    p.stop()

    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")
    results = []

    for job in jobs:
        link = f"https://www.wanted.co.kr{job.find('a')['href']}"
        title = job.find("strong", class_="JobCard_title__ddkwM").text
        company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
        location = job.find("span", class_="JobCard_location__2EOr5").text
        
        job = {
            "link": link,
            "company": company_name.replace(",", " "),
            "location":location.replace(",", " "),
            "position":title.replace(",", " "),
        }
        results.append(job)
    return results