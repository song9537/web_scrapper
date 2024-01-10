from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.wanted import extract_wanted_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
wanted = extract_wanted_jobs(keyword)

jobs = indeed + wwr + wanted

file = open(f"{keyword}.csv", "w", encoding="utf-8")

file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()