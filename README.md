# WEB SCRAPING-MISSION TO MARS

## Objective
In this project we built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Steps 
- Step 1 - Scraping

### NASA Mars News
-Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. 
### JPL Mars Space Images - Featured Image
* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
### Mars Weather
* Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page. 
### Mars Facts
* Visit the Mars Facts webpage [here](http://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
### Mars Hemispheres
* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres and title.

- Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

## Skills
Python, Flask, MongoDB, PyMongo, Pandas, Splinter, BeautifulSoup, HTML, CSS, Bootstrap, Heroku

## Mars Facts HTML page

![alt text](https://github.com/Lalitaeranki/Web_scraping/blob/master/mars.png)
