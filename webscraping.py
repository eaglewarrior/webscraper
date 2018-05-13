from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
Uclient=uReq(my_url)
page_html=Uclient.read()
Uclient.close()
#this dos the html parsing
page_soup=soup(page_html,"html.parser")
#finding out specific tag
page_soup.p
page_soup.h1
page_soup.body.span
page_soup.body.span
#now for each graphic card in item-container tag
#grab this product
containers=page_soup.findAll("div",{"class":"item-container"})
len(containers)#for knowing how many product is there
containers[0]#to know first product html
filename="products.csv"
f=open(filename, "w")
headers="brand, product_name, shipping\n"
f.write(headers)
for container in containers:
	brand=container.div.div.a.img["alt"]#it gives hieracy and grabs title name of product
	title_container=container.findAll("a",{"class":"item-title"})
	product_name=title_container[0].text#for text
	shipping_container=container.findAll("li",{"class":"price-ship"})
	shipping=shipping_container[0].text.strip()#strip removes the white space
	print("brand: "+brand)
	print("product_name: " +product_name)
	print("shipping: " +shipping)

	f.write(brand + "," +product_name.replace(",","|") + ","+ shipping +"\n")
f.close()







