from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

page_url = "https://www.cognizant.com"

uClient = urlopen(page_url)

page_soup = soup(uClient.read(),"html.parser")

uClient.close()

def getContent(tag,attr,attr_name,page_soup):
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


def getLink(tag,attr,attr_name,page_soup):
    menu_items = page_soup.findAll(tag,{attr:attr_name})
    contents =[]

    for menu_item in menu_items:
 
        menu_link = menu_item.get('href')
        if menu_link[0] == '/':
            link = page_url + menu_link
        else:
            link = menu_link
        contents.append(link)
    return contents

def getLinkbytag2(tag,tag2,attr,attr_name,pg_soup,page_url):
    contents =[]
    for menu_ul in pg_soup.find_all(tag,{attr:attr_name}):
        for menu_item in menu_ul.find_all(tag2):
            if(menu_item.find('a')):    
                menu_link = menu_item.find('a').get('href')
                if menu_link:
                    if menu_link[0] == '/':
                        link = page_url + menu_link
                    else:
                        link = menu_link
                contents.append(link)
    return contents

def getLinkbytag(tag,attr,attr_name):
    menu_items = page_soup.findAll(tag,{attr:attr_name})
    contents =[]

    for menu_item in menu_items:

        if menu_item.text.strip().lower().find('about') != -1:
            break

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


technos = set()

menu_list = getContent("h2","class","entry-title",page_soup)
technos.update(getTech(menu_list))

content = getContent("div","class","et_pb_text_inner",page_soup)
technos.update(getTech(content))

menu_link_list = getLinkbytag("li","class","arrow-end")

for link in getLink("a","title","Learn More",page_soup):
    menu_link_list.append(link)

print("home: \n")
for technology in technos:
    print(technology)

menu_items_list = set()

for link in menu_link_list:
    technologies = set()
    pg_url = link

    pg_soup = soup(urlopen(pg_url).read(),"html.parser")
    # print("\n" +link)

    for link in getLinkbytag2("ul","li","class","menu p1 relative medium-absolute submenu is-dropdown-submenu first-sub vertical",pg_soup,page_url):
        menu_items_list.add(link)
        # print(link)

    urlopen(page_url).close()
    
    menu_list = getContent("h3","class","card_default__title",pg_soup)
    technologies.update(getTech(menu_list))

    content = getContent("div","class","et_pb_tab_content",pg_soup)
    technologies.update(getTech(content))

    # content_desc = getmenu_items("p")
    # technologies.update(getTech(content_desc))

    # content = getmenu_items("span")
    # technologies.update(getTech(content))

    for technology in technologies:
        print(technology)

for link in menu_items_list:

    techs =set()

    urlClient = urlopen(link)
    print(link)

    pg2_soup = soup(urlClient.read(),"html.parser")

    urlClient.close()
    
    content = getContent("div","class","media-object-section w100",pg2_soup)
    techs.update(getTech(content))

    content = getContent("div","class","small-12",pg2_soup)
    techs.update(getTech(content))

    content = getContent("div","class","column column-block flex-container",pg2_soup)
    techs.update(getTech(content))

    for technology in techs:
        print(technology)