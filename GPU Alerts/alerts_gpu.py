import smtplib
import time
from requests import request
from bs4 import BeautifulSoup as soup


def send_email(link_to_gpu):
	content = f'A GPU is in Stock at the following link: {link_to_gpu}'
	mail=smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login('email','password')
	mail.sendmail('fromemail','emailrecepient',content)
	mail.close()

def check_bestbuy(URL):
	
	in_stock = False
	user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"
	r = request.get(URL, headers = {'User-agent':user_agent})
	if 'Sold Out' in r.text:
		in_stock = False
	else:
		in_stock = True

	return in_stock

# Check if GPUs are in stock
GPU_LINK_LIST = []


for link in GPU_LINK_LIST:
	time.sleep(3)
	
	if check_bestbuy(link):
		send_email(link)
	

