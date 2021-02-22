import requests as r
from bs4 import BeautifulSoup

def start():
    print("LOOKING FOR JOBS!!!!!\n\n")
    job_title = input("Job Title: ")
    job_loc = input("Job Location (country): ")
    URL = 'https://www.monster.com/jobs/search/?q='+ job_title+'&where='+job_loc
    return URL
URL = start()
page = r.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section',class_='card-content')

for job_elem in job_elems:
    #each job_elem is a new BeautifullSoup object

    title_elem = job_elem.find('h2',class_="title")
    company_elem = job_elem.find('div',class_="company")
    location_elem = job_elem.find('div',class_="location")
    
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
