import smtplib
import time
import requests as request
from bs4 import BeautifulSoup as soup

email = input("Enter your gmail to send from: ")
password = input("Enter your gmail password to send from: ")
email_rec = input("Enter Gmail to send to:" )

# Check Email Credentials
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email, password)
mail.close()

def send_email(link_to_gpu):
	content = f'A GPU is in Stock at the following link: {link_to_gpu}'
	mail=smtplib.SMTP('smtp.gmail.com',587)
	mail.ehlo()
	mail.starttls()
	mail.login(email, password)
	mail.sendmail('fromemail', email_rec, content)
	mail.close()

def check_bestbuy(URL):
	print('___________________________________________')
	print(f'Checking {URL}')
	in_stock = False
	user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3"
	r = request.get(URL, headers = {'User-agent':user_agent})
	
	if 'Access Denied' in r.text:
		print("Something went wrong")
		exit()
	
	if 'Sold Out' in r.text:
		in_stock = False
		print('Sold Out\n\n\n')
	else:
		in_stock = True

	return in_stock

# Open Bestbuylist 
GPU_LINK_LIST = []
with open('bestbuy_gpus.txt', 'r', encoding='utf-8') as temp:
	for line in temp:
		if line != '\n':
			GPU_LINK_LIST.append(line.replace('\n',''))


# TODO - Use threading to make multiple requests to the different links in list

count = 0
x = True
while x == True:
	print(f'Times Looped: {count}')
	for link in GPU_LINK_LIST:
		time.sleep(.01)
		if check_bestbuy(link):
			send_email(link)
			print('GPU found to be in Stock. Email Notification Sent!')
	count +=1