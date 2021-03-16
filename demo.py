from bs4 import BeautifulSoup
def pretty(html):
	return BeautifulSoup(str(html), 'html.parser').prettify()