import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(jpg,img_url):
	req = urllib.request.urlopen(img_url)

	img_content = req.read()

	with open(jpg, "wb") as f:
		f.write(img_content)


def main():
	gevent.joinall([
		gevent.spawn(downloader, "1.jpg", "https://cnet1.cbsistatic.com/img/-B3kmqxu8sB6pYlTVZqRF9_cJB0=/2020/04/16/7d6d8ed2-e10c-4f91-b2dd-74fae951c6d8/bazaart-edit-app.jpg"),
		gevent.spawn(downloader, "2.jpg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/110px-Python-logo-notext.svg.png")
	])
	

if __name__ == "__main__":
	main()


