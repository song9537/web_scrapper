from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from bs4 import BeautifulSoup

base_url = "https://ca.indeed.com/jobs?q="
search_term = "python"

driver = webdriver.Chrome()
driver.get(f"{base_url}{search_term}")

soup = BeautifulSoup(driver.page_source, "html.parser")
job_list = soup.find("ul", class_="css-zu9cdh eu4oa1w0")
jobs = job_list.find_all('li', recursive=False)

for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        print("job li")
    else:
        print("mosaic li")


while(True):
    pass
