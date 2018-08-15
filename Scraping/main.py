
import urllib.request 
from bs4 import BeautifulSoup
address="https://www.rottentomatoes.com/m/incredibles_2/reviews/"

page=urllib.request.urlopen(address)
soup= BeautifulSoup(page,'html.parser')
#print (soup.prettify())

review = soup.find_all('div', attrs={'class':'the_review'})
#print(review)

for i in review:
	print("Review :")
	print(i.get_text(),"\n")