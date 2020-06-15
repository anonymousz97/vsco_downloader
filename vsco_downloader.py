from bs4 import BeautifulSoup
import requests
import random
import shutil

def download():
	url = input('Input VSCO url : ')

	res = requests.get(url)
	bs = BeautifulSoup(res.content,'html.parser')
	#print(str(res.content).find('disableSave-mobile css-6dp941'))
	#print(res.content)

	link = str(bs.find("meta",property="og:image",content=True).get("content",None))
	link = link[:link.rfind('?')]
	hash = random.getrandbits(64)
	hash = str(hash)+".jpg"
	response = requests.get(link, stream=True)
	with open(hash, 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response
	print("Done! Saved as {}".format(hash))


if __name__ == "__main__":
	download()