#タイトルを引っ張てくる

import requests,bs4
res = requests.get('http://www.yamaguchi-u.ac.jp/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup.title)
