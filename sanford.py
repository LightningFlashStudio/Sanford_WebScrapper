import bs4
import discord

from discord.ext.commands import Bot
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&Chipset%252FGPU%2520Manufacturer=AMD&Memory%2520Type=GDDR5&_nkw=graphics%20card&_dcat=27386&rt=nc&Chipset%252FGPU%2520Model=AMD%2520Radeon%2520R7%2520360%7CAMD%2520Radeon%2520R7%2520370%7CAMD%2520Radeon%2520R9%2520270%7CAMD%2520Radeon%2520R9%2520270X%7CAMD%2520Radeon%2520R9%2520280X%7CAMD%2520Radeon%2520R9%2520290%7CAMD%2520Radeon%2520R9%2520290X%7CAMD%2520Radeon%2520R9%2520380%7CAMD%2520Radeon%2520R9%2520380X%7CAMD%2520Radeon%2520R9%2520390%7CAMD%2520Radeon%2520R9%2520390X%7CAMD%2520Radeon%2520RX%2520470%7CAMD%2520Radeon%2520RX%2520480'
# opening up the connection, grabbing the page.
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parsing the html
page_soup = soup(page_html, "html.parser")


# grabbing each product
containers = page_soup.findAll("li",{"class":"sresult lvresult clearfix li"})