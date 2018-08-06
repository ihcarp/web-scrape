from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

page_url = "https://www.tcs.com/"

uClient = urlopen(page_url)

page_soup = soup(uClient.read(),"html.parser")

uClient.close()

def getContent(tag,attr,attr_name):
    content_topics = page_soup.findAll(tag,{attr:attr_name})
    content =set()
    for content_topic in content_topics:
        content_title = content_topic.text
        content.add(content_title)
    return content

def getTech(desc):
    f1 = open("tech.txt","r")

    tech_list=[]
    for line in f1:
        tech_list.append(line.strip())
    f1.close()

    techs = set()
    for sentence in desc:
        for tech in tech_list:
            if tech.isupper():
                if sentence.find(tech) != -1:
                    techs.add(tech)
            else :
                if sentence.lower().find(tech.lower()) != -1:
                    techs.add(tech)
    return techs

technologies = set()

menu_list = getContent("li","class","menu-item-contents")
technologies.update(getTech(menu_list))

content = getContent("div","class","bcl-title")
technologies.update(getTech(content))

content_desc = getContent("div","class","bcl-desc")
technologies.update(getTech(content_desc))

print("home: \n")
for technology in technologies:
    print(technology)


