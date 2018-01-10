'''
Script to fetch the currency exchange rate of GBP-USD from xe.com,
with pseudocode below for further updates (if interested in being alerted of the rate going above a certain threshold).
This is a basic web-scraping script, following a workshop I attended on Python and web scraping, where we scraped Amazon.com, and a PDF.
(For Amazon, we fetched a product price and then compared it (on a basic level) to other "people also viewed" products in the same category, to find the lowest price).

The following uses BeautifulSoup and requests to fetch the GBP-USD xe.com URL, get the rate, and display it. 
Further pseudocode below for improvisations and automation.
'''

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=USD" # Currency rate GBP-USD
page = requests.get(url, headers=headers)
bsobj = BeautifulSoup(page.content, "html.parser")

rate = bsobj.find("span",{"class":"uccResultAmount"}) # returns the full <span> tag including the exchange rate
print(rate.get_text()) # prints the rate

# I actually want to be notified if the rate goes above a certain threshold, in case I want to trade in the currency at the rate.
# Here is the pseudocode:

'''
Pseudocode:

    threshold = {get value from database}
    last-email-send = {get value from database, to tell when we last sent an email from this script}
    
    if (rate <= threshold and last-email-send + 12 hours <= now):
        send email to me with a reminder, or send alert via API of preferred system for notification
        store last-email-send date in database, so that we won't spam the recipient!
    
Notes:
    We need to ensure this is run as a cron every hours or 'x' hours depending on how regularly we want to check the exchange rate
'''
