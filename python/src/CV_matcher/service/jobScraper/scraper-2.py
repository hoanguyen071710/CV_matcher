import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    # site_name=["indeed", "linkedin", "zip_recruiter", "glassdoor"],
    site_name=["linkedin"],
    search_term="Grab",
    location="Indonesia",
    results_wanted=50,
    hours_old=120, # (only Linkedin/Indeed is hour specific, others round up to days old)
    country_indeed='Vietnam',  # only needed for indeed / glassdoor
    
    # linkedin_fetch_description=True # get full description , direct job url , company industry and job level (seniority level) for linkedin (slower)
    # proxies=["208.195.175.46:65095", "208.195.175.45:65095", "localhost"],
    
)
print(f"Found {len(jobs)} jobs")
print(jobs['job_url'])
# jobs.to_csv("jobs.csv", quoting=csv.QUOTE_NONNUMERIC, escapechar="\\", index=False) # to_excel