import bs4
import ssl
import json
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#importing soup library as well as making BeautifulSoup easy to use as soup

my_url = 'http://www.ucdenver.edu/pages/ucdwelcomepage.aspx'
#giving url link to go scrape

context = ssl._create_unverified_context()

#creating a secure socket layer verification

uClient = uReq(my_url, context=context) #accessing the url

page_html = uClient.read()#reading the html data

uClient.close()#closing the client

page_soup = soup(page_html, "html.parser")#parsing through the html data using soup

#finding all scripts and assigning to container.
containers = page_soup.findAll("script",{"type":"application/ld+json"}) 

#creating container with data loaded in json for first element in containers, stripping the text as well.
dept_containers = json.loads(containers[0].text.strip())

#json.dumps(dept_containers)

departments = dept_containers["department"] #scraping department from dept_container

jsonfile = open("department.json", "w")#creating a department.json file

new_list = [] #new list

for dep in departments: #for each element inside departments we are storing the name, telephone, and url into new_department {}

    new_department = {}
    new_department["name"] = dep.get("name", "Not available")
    new_department["telephone"] = dep.get("telephone", "Not found")
    new_department["url"] = dep.get("url", "Not found")
    new_list.append(new_department)#creating dictionary
    #print(new_list)

jsonList = json.dumps(new_list)#turning dictionary into a string and .dumping into a list
jsonfile.write(jsonList) #outputting elements to file
jsonfile.close()#closing file.
