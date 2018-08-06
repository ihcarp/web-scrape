from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

page_url = "https://www.tcs.com"

uClient = urlopen(page_url)

page_soup = soup(uClient.read(),"html.parser")

uClient.close()

def getContent(tag,attr,attr_name):
    content_topics = page_soup.findAll(tag,{attr:attr_name})
    content =[]
    for content_topic in content_topics:
        content_title = content_topic.text
        content.append(content_title)
    return content

def getmenu_items(tag):
    result_contents = page_soup.findAll(tag)
    contents = []
    for content in result_contents:
        content_text = content.text
        contents.append(content_text)
    return contents

def getLinkbytag(tag,attr,attr_name):
    menu_items = page_soup.findAll(tag,{attr:attr_name})
    contents =[]

    for menu_item in menu_items:

        if(menu_item.find('a')):    
            menu_link = menu_item.find('a').get('href')
            if menu_link[0] == '/':
                link = page_url + menu_link
            else:
                link = menu_link
            contents.append(link)
    return contents


def getTech(desc):
    f1 = open("tech.txt","r")
    tech_list=set()
    for line in f1:
        tech_list.add(line.strip())
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

# menu_items = page_soup.findAll("li",{"class":"menu-item-contents"})

# menu_link_list =[]
# for menu_item in menu_items:
#     if menu_item.text.strip().lower().find('about') != -1:
#         break

#     if(menu_item.find('a')):    
#         menu_link = menu_item.find('a').get('href')
#         if menu_link[0] == '/':
#             link = page_url + menu_link
#         else:
#             link = menu_link
#         menu_link_list.append(link)
#             # print(link)

menu_link_list = getLinkbytag("li","class","menu-item-contents")

for link in menu_link_list:
    technologies = set()
    page_url = link

    page_soup = soup(urlopen(page_url),"html.parser")
    print("\n" +link)

    urlopen(page_url).close()
    
    content_topics = getContent("div","class","cws-card-heading")
    technologies.update(getTech(content_topics))

    card_desc = getContent("div","class","cws-card-description")
    technologies.update(getTech(card_desc))

    content = getContent("h1","class","hero-main-message")
    technologies.update(getTech(content))

    content_desc = getContent("h2","class","hero-sub-message")
    technologies.update(getTech(content_desc))

    for technology in technologies:
        print(technology)

