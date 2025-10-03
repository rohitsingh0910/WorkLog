import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.freelancer.in/jobs/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

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

df = pd.DataFrame(data)
df.to_csv("freelancer_projects_india.csv", index=False)
print("✅ Scraped and saved to 'freelancer_projects_india.csv'")
