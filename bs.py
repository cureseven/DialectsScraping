#テキストを引っ張てくる
#テキストファイルに書き込む

import requests, bs4

for i in range(9):
    title = "https://dictionary.goo.ne.jp/srch/dialect/%E7%BE%A4%E9%A6%AC/" + "m9p" + str(i+1) + "u/"
    # print(title)
    res = requests.get(title)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # elems = soup.select('body')

    elems = soup.find_all("dt", class_="title search-ttl-a")
    # if image -> ｶﾞ 

    filetitle = "gunma" + str(i+1) + ".txt"

    f=open(filetitle,'w',encoding='utf-8')

    for elem in elems:
        print(elem.getText())
        f.write(elem.getText())

        f.close
