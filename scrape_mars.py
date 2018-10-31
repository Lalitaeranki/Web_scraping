
# coding: utf-8

# In[104]:


# Import BeautifulSoup
# Import Splinter and set the chromedriver path
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymongo
import tweepy
import requests
from splinter import Browser
import time


# In[105]:


#Function to call the chrome browser
def browser_func():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = browser_func()
    # create mars_data dict that we can insert into mongo
    mars= {}
# In[ ]:
#mars.update function

    # Visit the following URL for article and title
    url = "https://mars.nasa.gov/news/" 
    # calling the function
    browser=browser_func()
    #Visit method to navigate through pages
    browser.visit(url)
    # the html attribute to get the html content of the visited page
    html = browser.html
    # document through Beautiful Soup gives us a BeautifulSoup object, which represents the document as a nested data structure
    soup = bs(html, 'html.parser')
    # navigate to find the title in content_title class and article in article teaser body
    news_title=soup.find('div',class_='content_title').text
    news_p=soup.find('div',class_="article_teaser_body").text
    #Print the results
    print(f'News Title: {news_title}')
    print(f'News Paragraph: {news_p}')
    mars["news_title"]=news_title
    mars["news_p"]=news_p



    # In[77]:


    # Visit the following URL for image url

    url_image="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser=browser_func()
    browser.visit(url_image) 


    # In[78]:


    #timer to navigate through pages
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)


    # In[79]:


    image_html = browser.html
    image_soup = bs(image_html, 'html.parser')
    temp_img_url = image_soup.find('img', class_='main_image')
    half_img_url = temp_img_url.get('src')
    #capturing the image url 
    featured_image_url = "https://www.jpl.nasa.gov" +half_img_url
    print(featured_image_url)
    mars["featured_image_url"]=featured_image_url


    # In[82]:


    #scrape the latest Mars weather tweet from the page
    Twitter_url="https://twitter.com/marswxreport?lang=en"
    browser=browser_func()
    browser.visit(Twitter_url)
    Twitter_html= browser.html
    Twitter_soup = bs(Twitter_html, 'html.parser')
    mars_weather=Twitter_soup.find('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)
    mars["mars_weather"]=mars_weather

    # In[83]:


    #Visit the Mars Facts webpage 
    mars_facts_url="https://space-facts.com/mars/"
    facts_table= pd.read_html(mars_facts_url)
   

    # In[85]:


    #use Pandas to scrape the table
    df=facts_table[0]
    df.columns=["Description","Value"]
    df.set_index('Description', inplace=True)
    df
   

    # In[100]:


    #Pandas to convert the data to a HTML table string
    html_table = df.to_html()

    table=html_table.replace("\n","")
    

    # In[102]:


   
    mars["mars_table"]=table
    # In[103]:


    #the USGS Astrogeology site to obtain high resolution images for each of Mar's hemispheres
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser=browser_func()
    browser.visit(hemispheres_url)
    html = browser.html
    soup =bs(html, "html.parser")
    hemisphere_image_urls = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=bs(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": image_url})



    # In[92]:


    hemisphere_image_urls
    mars["hemisphere_image_urls"]=hemisphere_image_urls

    return mars
# In[95]:



