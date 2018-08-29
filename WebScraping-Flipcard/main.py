from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReg

my_url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient = uReg(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("div", {"class": "_3O0U0u"})
#print(len(containers))

#print(soup.prettify(containers[0]))

container = containers[0]
#print(container.div.img["alt"])

price = container.find_all("div", {"class":"col col-5-12 _2o7WAb"})
#print(price[0].text)

ratings = container.find_all("div", {"class":"niH0FQ"})
#print(ratings[0].text)

filename = "products.csv"
f = open(filename,"w")

headers = "Product_name,Pricing,Ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.find_all("div", {"class":"col col-5-12 _2o7WAb"})
    price = price_container[0].text.strip()

    rating_container = container.find_all("div", {"class":"niH0FQ"})
    rating = rating_container[0].text

    #print("product_name:"+ product_name)
    #print("price:" + price)
    #print("rating:" + rating)

    #String parsing
    trim_price = ''.join(price.split(','))
    rm_ruppe = trim_price.split("₹")
    ad_rs_price = "Rs." + rm_ruppe[1]
    split_price = ad_rs_price.split('E')
    final_price = split_price[0]

    split_rating = rating.split(" ")
    final_rating = split_rating[0]

    print(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")
    f.write(product_name.replace(",", "|") + "," + final_price + "," + final_rating + "\n")

f.close()