from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs

keyword = input("What do you want to search for?")


indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
