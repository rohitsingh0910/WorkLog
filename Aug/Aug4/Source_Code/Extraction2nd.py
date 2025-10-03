from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setup Chrome headless
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

driver.get("https://www.freelancer.in/jobs/")
time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
projects = soup.select('.JobSearchCard-item')

data = []
for job in projects:
    try:
        title = job.select_one('.JobSearchCard-primary-heading-link').text.strip()
        desc = job.select_one('.JobSearchCard-primary-description').text.strip()
        budget = job.select_one('.JobSearchCard-secondary-price').text.strip()
        techs = [t.text.strip() for t in job.select('.JobSearchCard-primary-tags li')]

        data.append({
            'title': title,
            'description': desc,
            'budget': budget,
            'technologies': ', '.join(techs)
        })
    except:
        continue

driver.quit()

df = pd.DataFrame(data)
df.to_csv("freelancer_projects_india_2nd.csv", index=False)
print("✅ Dynamic scrape complete — CSV saved")
