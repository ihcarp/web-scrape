from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

page_url = "https://www.accenture.com"

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
            if menu_link[0] != '#':
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



menu_list = getContent("h2","class","headline")
technos.update(getTech(menu_list))

content = getContent("p","class","subHeadline")
technos.update(getTech(content))

menu_link_list = getLinkbytag("li","class","col-sm-3 secondary-item")

for link in getLinkbytag("li","class","col-sm-3 tertiary-item"):
    menu_link_list.append(link)

print("home: \n")
for technology in technos:
    print(technology)
    
for link in menu_link_list:
    technologies = set()
    page_url = link

    page_soup = soup(urlopen(page_url),"html.parser")
    print("\n" +link)

    urlopen(page_url).close()
    
    page_title = getContent("h1","class","page-title")
    technologies.update(getTech(page_title))

    content_topics = getContent("h2","class","headline")
    technologies.update(getTech(content_topics))

    card_content = getmenu_items("p")
    technologies.update(getTech(card_content))

    card_desc = getContent("p","class","cws-card-description")
    technologies.update(getTech(card_desc))

    p_fluid = getContent("p","class","fluid")
    technologies.update(getTech(p_fluid))

    content = getContent("h3","class","c-card__title")
    technologies.update(getTech(content))

    content_desc = getmenu_items("h4")
    technologies.update(getTech(content_desc))

    div_media = getContent("div","class","media")
    technologies.update(getTech(div_media))

    div_module_body = getContent("div","class","module-body")
    technologies.update(getTech(div_media))

    p_desc = getContent("p","class","description")
    technologies.update(getTech(p_desc))
 
    technologies.update(getTech(getContent("h3","class","module-title")))
    
    technologies.update(getTech(getContent("p","class","card-description")))

    h_sub = getContent("h2","class","subsection-title")
    technologies.update(getTech(h_sub))

    for technology in technologies:
        print(technology)



    