# module for searching the pages and downloading source code of the page
from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def By_Link(link):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}

    driver = webdriver.Firefox()
    driver.get("https://images.google.com")
    time.sleep(5)

    driver.find_element_by_xpath("//span[contains(@class,'BwoPOe')]").click()  # clicking on camera icon
    # this section is for find by image path
    # driver.find_element_by_xpath("//input[contains(@name,'encoded_image')]").send_keys("~/Desktop/minor_project/download.jpeg")

    # This section is for find by link path
    # driver.find_element_by_xpath("//a[contains(.,'Upload an image')]").click()
    driver.find_element_by_xpath("//input[@name='image_url']").send_keys(link)  # pasting the link
    driver.find_element_by_xpath("//input[@name='image_url']").send_keys(Keys.ENTER)  # pressing search button

    time.sleep(10)
    url = driver.current_url + "&as_qdr=y15"
    driver.get(url)

    source = driver.page_source
    # print(source)
    return source


### This function will find the image by uploading it
def by_File(imgpath):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'
    }

    driver = webdriver.Firefox()
    driver.get("https://images.google.com")
    time.sleep(5)
    print('inside the function')
    driver.find_element_by_xpath("//span[@class='BwoPOe']").click()  # clicking on camera icon
    driver.find_element_by_xpath("//a[contains(.,'Upload an image')]").click()
    driver.find_element_by_xpath("//input[contains(@name,'encoded_image')]").send_keys(
        imgpath)  # driver.find_element_by_xpath("//a[contains(.,'Upload an image')]").send_keys(Keys.ENTER)

    time.sleep(10)
    url = driver.current_url + "&as_qdr=y15"
    driver.get(url)
    source = driver.page_source
    # print(source)
    return source


'''if __name__ == '__main__':
    by_File("/home/sachin/Desktop/minor_project/download.jpeg")



'''

'''
    # Finding all the elements with h3 tags i.e. website headings

    soup = BeautifulSoup(source,"lxml")
    #print(soup.prettify())
    title=soup.find_all('h3')
    dates = soup.find_all(class_='f')
    links = soup.find_all('a')
    for h3,f in zip(title,dates):
        print(h3)
        print(f)

    for i in links:
        print(i)



url = driver.current_url + "&as_qdr=y15"
driver.get(url)
1. Use selenium
2. launch browser in headless mode
3. upload image or pass the link
4. automate the process and click on the search image by url
5. Get the list of top websites lets say 20 top websites
6. search each website link publication date by searching on google as inurl:link then in resulted url add "&as_qdr=y15" in the end.
7. it will result in the pages with publication date...
8. Just scrap them
5. Then scrap the search result or just get the url of search result page
6. filter out the url
7. 



'''
