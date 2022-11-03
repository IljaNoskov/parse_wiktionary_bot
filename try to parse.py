import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import os
os.system('chcp 65001')


URL_TEMPLATE = "https://ru.wiktionary.org/wiki/%D0%BF%D1%91%D1%81"
r = requests.get(URL_TEMPLATE)
#print(r.text)
#f=open('text.txt','w+',encoding="utf-8")
#f.write(r.text)
#f.close()

#<p><b>пёс</b>&#160;(<span title="написание в дореформенной орфографии" style="border-bottom: 1px dotted; cursor: help">дореформ.</span> <span style="font-family:&#39;Palatino Linotype&#39;"><a href="/w/index.php?title=%D0%BF%D1%91%D1%81%D1%8A&amp;action=edit&amp;redlink=1" class="new" title="пёсъ (страница не существует)">пёсъ</a></span>)
#</p><p><a href="/wiki/%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5" title="существительное">Существительное</a>, одушевлённое, мужской род, 2-е <a href="/wiki/%D1%81%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5" title="склонение">склонение</a>&#32;(тип склонения 1*b  по <a href="/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C:%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8F_%D0%97%D0%B0%D0%BB%D0%B8%D0%B7%D0%BD%D1%8F%D0%BA%D0%B0" title="Викисловарь:Использование словаря Зализняка">классификации А.&#160;А.&#160;Зализняка</a>).
#</p><p>Корень: <b>-пёс-</b> <span class="source" style="font-size: x-small;">&#91;<a href="/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C:%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%82%D1%83%D1%80%D1%8B#Тихонов-1996" title="Викисловарь:Список литературы">Тихонов, 1996</a>&#93;</span>.
#</p>

soup=bs(r.text,'html.parser')
opr=soup.find_all('a', href="/wiki/%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5")
print(opr)
print(soup.get_text())
for name in opr:
    print(name)
