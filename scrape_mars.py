# Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape 
# that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

def scrape():

    browser = init_browser()
    scraped_data ={}

    # NASA Mars News
    mars_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news_url)
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')
    news_title = mars_news_soup.find('div', class_='content_title').text
    news_p = mars_news_soup.find('div', class_='article_teaser_body').text

    # JPL Mars Space Images - Featured Image
    space_images_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(space_images_url)
    html = browser.html
    space_images_soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = space_images_soup.find('article', class_='carousel_item')
    footer = featured_image_url.find('footer')
    ref = footer.find('a')
    path = ref['data-fancybox-href']
    featured_image_url = ('https://www.jpl.nasa.gov' + path)

    # Mars Weather
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find('a')

    # Mars Facts
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)
    mars_facts = pd.read_html(mars_facts_url)[0]
    mars_facts.columns=["Description","Values"]

    # Mars Hemispheres

    # Cerberus
    url_cerberus = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_cerberus)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')   
    url_cerberus = soup.find('div', class_='downloads')
    link = url_cerberus.find('a')
    cerberus = link['href']

    # Schiaparelli
    url_schiaparelli = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url_schiaparelli)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    url_schiaparelli = soup.find('div', class_='downloads')
    link = url_schiaparelli.find('a')
    schiaparelli = link['href']

    # Syrtis
    url_syrtis = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_syrtis)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    url_syrtis = soup.find('div', class_='downloads')
    link = url_syrtis.find('a')
    syrtis = link['href']   

    # Valles
    ulr_valles = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(ulr_valles)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    ulr_valles = soup.find('div', class_='downloads')
    link = ulr_valles.find('a')
    valles = link['href']
    
    # Mars Dictionary
    
    scraped_data = {
        "Mars News Title": news_title,
        "JPL Mars Space Images ": news_p,
        "Mars Weather": mars_weather,
        "Mars Facts": mars_facts,
        'Valles Marineris Hemisphere':valles,
        'Syrtis Major Hemisphere':syrtis,
        'Schiaparelli Hemisphere':schiaparelli,
        'Cerberus Hemisphere':cerberus
        
    }

    return scraped_data