import openpyxl,bs4,requests,os
res=requests.get("https://www.imdb.com/list/ls075558108/?sort=list_order,asc&st_dt=&mode=simple&page=1&ref_=ttls_vw_smp")
type (res)
res.text
res.raise_for_status()
objsoup=bs4.BeautifulSoup(res.text,features="html.parser")
type(objsoup)
lista=objsoup.select('div')
type(lista)
lista(1)