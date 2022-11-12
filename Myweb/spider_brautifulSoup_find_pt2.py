from bs4 import BeautifulSoup

html="""
<body><p class="myclass1">
<a id="myid1" herf="link1">我的連結1</a>
<a id="myid2" herf="link2">我的連結2</a>
<a id="myid3" herf="link3">我的連結3</a>
<a id="myid4" herf="link4">我的連結4</a>
</p></body>
"""

#以BeautifulSoup解析的網頁內容為html，html.parser為方法
#sp為網頁結構
sp=BeautifulSoup(html,"html.parser")

#搜尋屬性為id=myid2，傳回第一個符合條件的標籤並設定給myid2_tag
myid2_tag= sp.find(id="myid2")


#p_tag:搜尋(往上搜尋)myid2_tag中的上一層<p>標籤，設定給p_tag
p_tag=myid2_tag.find_parent("p")
print(p_tag)#<p><a...><a...><a...><a...></p>

#link_tag:搜尋myid2_tag同一層中往前的<a>標籤，設定給link_tag
link_tag=myid2_tag.find_previous_sibling("a")

print("-"*20)
print(link_tag)