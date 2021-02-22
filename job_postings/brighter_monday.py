import requests as r
from bs4 import BeautifulSoup as bs

posts = ['accounting-auditing-finance','admin-office','building-architecture','community-social-services','consulting-strategy','creative-design','customer-service-support','driver-transport-services','engineering-technology','farming-agriculture','health-safety','human-resources','legal-services','management-business-development','marketing-communications','medical-pharmaceutical','product-project-management','quality-control-assurance','research-teaching-training','sales','software-data','supply-chain-procurement','trades-services']

def start(posts):
    URL = 'https://www.brightermonday.co.ug/jobs'
    print("\u001b[47;1mWHICH JOB ARE YOU LOOKING FOR??\u001b[0m ")
    i =0
    for post in posts:
        print(f"{str(i)} : {post.capitalize()}")
        i= i+1
    USER_INPUT = int(input("Enter the job number here: "))

    for post in posts:
       if post == posts[USER_INPUT]:
            print(f"Looking for\u001b[33;1m {posts[USER_INPUT]}\u001b[0m Jobs ")
            print()
            return URL+'/'+ posts[USER_INPUT]

def init():
    URL = start(posts)
    page = r.get(URL)
    soup = bs(page.content,'html.parser')

    main_content = soup.find(class_="search-main__content")
    job_elems = main_content.find_all("article", class_="search-result")


    for job_elem in job_elems:
        job_title = job_elem.find('h3')
        try:
            job_c = job_elem.select('div.search-result__job-meta > a')[0]
            job_func = job_elem.select('div.ellipses > span')[0]
            job_desc = job_elem.select('div.search-result__content > p')[0]
        except IndexError:
            pass
        job_location = job_elem.find('div',class_='search-result__location')
    
        if None in (job_title,job_c, job_location,job_func,job_desc):
            continue
        print(f"\u001b[36;1mJOB TITLE:\u001b[31;1m {job_title.text.strip()}\u001b[0m")
        print(f"\u001b[36;1mCOMPANY:\u001b[31;1m {job_c.text.strip()}\u001b[0m")
        print(f"\u001b[36;1mLOCATION:\u001b[31;1m {job_location.text.strip()}\u001b[0m")
        print(f"\u001b[36;1mJOB FUNCTION:\u001b[31;1m {job_func.text.strip()}\u001b[0m")
        print(f"\u001b[36;1mJOB DESCRIPTION:\u001b[0m {job_desc.text.strip()}\u001b[0m")
        print()

init()
