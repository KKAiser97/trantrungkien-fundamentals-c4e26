from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
con = urlopen(url)
raw_data = con.read() 
page_content = raw_data.decode("utf8")
soup = BeautifulSoup(page_content, "html.parser")
ul = soup.find("ul","")
li_list = ul.find_all("li")
top_songs=[]
for li in li_list:
    h3= li.h3
    a= h3.a
    title = a.string
    h4 = li.h4
    a= h4.a
    artist = a.string
    top = {
    "artist":artist,
    "title": title
    }
    top_songs.append(top)
pyexcel.save_as(records=top_songs, dest_file_name="Top_songs.xls")
options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 10
    }
dl = YoutubeDL(options)
dl.download([title])