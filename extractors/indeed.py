from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_page_count(keyword):
    
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    base_url = "https://ca.indeed.com/jobs?q="
    driver = webdriver.Chrome(options=options)
    driver.get(f"{base_url}{keyword}")
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    pagination = soup.find("ul", class_="css-1g90gv6 eu4oa1w0")
    if pagination == None:
        return 1
    pages = pagination.find_all("li", recursive=False)
    page_num = len(pages)
    if page_num >= 5:
        return 5
    else:
        return page_num

def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")
    results = []
    for page in range(pages):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        driver = webdriver.Chrome(options = options)
        base_url = "https://ca.indeed.com/jobs"
        final_url = f"{base_url}?q={keyword}&start={page*10}"
        print("Requesting", final_url)
        driver.get(final_url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_list = soup.find("ul", class_="css-zu9cdh eu4oa1w0")
        jobs = job_list.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", attrs={"data-testid": "company-name"})
                location = job.find("div", attrs={"data-testid": "text-location"})
                
                job_data = {
                            'link': f"https://ca.indeed.com/{link}",
                            'company': company.string.replace(",", " "),
                            'location': location.string.replace(",", " "),
                            'position': title.replace(",", " ")
                        }
                
                results.append(job_data)
    return results
