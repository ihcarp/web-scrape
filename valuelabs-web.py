from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

page_url = "https://www.valuelabs.com/"

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


technologies = set()

menu_list = getContent("h2","class","entry-title")
technologies.update(getTech(menu_list))

content = getContent("div","class","col-md-12 text-left")
technologies.update(getTech(content))

content = getmenu_items("span")
technologies.update(getTech(content))

content = getContent("div","class","digital-info")
technologies.update(getTech(content))

menu_link_list = getLinkbytag("li","class","menu-item-type-post_type")

print("home: \n")
for technology in technologies:
    print(technology)
    
for link in menu_link_list:
    technologies = set()
    page_url = link

    page_soup = soup(urlopen(page_url),"html.parser")
    print("\n" +link)

    urlopen(page_url).close()
    
    # menu_list = getContent("h3","class","card_default__title")
    # technologies.update(getTech(menu_list))

    content = getContent("div","class","et_pb_tab_content")
    technologies.update(getTech(content))

    technologies.update(getTech(getContent("ul","class","bullets-list")))

    content_desc = getmenu_items("p")
    technologies.update(getTech(content_desc))

    content = getmenu_items("span")
    technologies.update(getTech(content))

    for technology in technologies:
        print(technology)