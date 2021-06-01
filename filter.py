# module for filtering important tags
from bs4 import BeautifulSoup
import re

'''def link_filter_date(page_Source):
    print('\n\n##################### RESULTS ARE SHOWN BELOW #############################')

    soup = BeautifulSoup(page_Source,"lxml")
    #print(f'this is the page source code :\n {soup.prettify()}')
    links=[]
    dates=[]
    a_tag = soup.find_all('a')  #findind all the source links
    for i in a_tag:
       try:
           if i['onmousedown'] and 'webcache' not in str(i['href']) and '/imgres?imgurl=' not in str(i['href']) :
               links.append(str(i['href']))
               print(i['href'])
       except:
           pass

    date = soup.find_all("span",{"class": "f"}) #finding all dates
    for i in date:
        i = str(i.text)
        i = i.replace('-','')
        i = i.strip()
        x = re.findall("[a-zA-Z].*[0-9]", i) # using regex for extraction of date
        dates.append(x[0])


    for i,j in zip(links,dates):
                print(f'Link Found :  {i} dated on {j}')
    print('Thank You for using this program')


'''


def link_filter_image(page_Source):
    print('\n\n##################### MOST MATCHING RESULTS ARE SHOWN BELOW #############################')
    # print(f"printing source {page_Source}")
    soup = BeautifulSoup(page_Source, "lxml")
    # print(f'this is the page source code :\n {soup.prettify()}')
    links = []
    dates = []
    a_tag = soup.find_all('a')  # findind all the source links
    prohibited = ['webcache', 'google.com', '/imgres?imgurl']
    for i in a_tag:
        try:
            if i['onmousedown'] and not (any(word in str(i) for word in prohibited)):
                links.append(str(i['href']))
                # print(i['href'])
        except:
            pass

    date = soup.find_all("span", {"class": "f"})  # finding all dates
    for i in date:
        i = str(i.text)
        i = i.replace('-', '')
        i = i.strip()
        # print(i)
        x = re.findall("[a-zA-Z]+ [0-9]+, [0-9]+", i) or re.findall("[0-9]+ [a-z]+ ago",i)  # Aug 15, 2020 or 5 days ago
        d = str(x[0])
        d = d.strip()
        # print(f"{x[0]}")
        dates.append(d)
    for i, j in zip(links[:], dates[:]): # Provide index in links[ : ] and dates[ : ] to print specific links
        print(f'Link Found :  {i} dated on {j}')
    print('Thank You for using this program')


# working till now(1:44 pm 12/5/20]

# /home/sachin/Desktop/minor_project/floyd.jpg


'''if __name__ == '__main__':
    with open("source_code.txt","r") as f:
        code = f.read()
        link_filter_image(code)
'''
