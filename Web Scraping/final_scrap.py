import requests
from bs4 import BeautifulSoup
import urllib.request
import codecs,time
import shutil,sys,os
from os import path

# url="https://turabit.com/"
# https://www.cims.org/vision-mission-values/
# https://www.shalby.org/about-us/about-shalby/
# https://zydushospitals.com/about_us.html
# https://www.sterlinghospitals.com/about/
# https://nidhihospital.org/about-us/
# http://www.kohinoorhospitals.in/kohinoorgroupindia
# https://www.zenhospital.in/about-hospital/
# https://www.jeavio.com/about
# https://www.crestdatasys.com/about-us/#
# https://arastusystems.com/views/about.html

# Not Acceptable!Not Acceptable!An appropriate representation of the requested resource could not be found on this server. This error was generated by Mod_Security.
# https://parthhospital.com/about-us/
# https://drparthvaishnav.com/about/

# HTTP Error 404: Not Found
# https://turabit.com/technology/

def get_path():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))
    else:
        return getattr(sys, '_MEIPASS', path.abspath(path.dirname(__file__)))

bash_path = get_path()
url = "https://turabit.com/"

# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# all_text = soup.get_text()

urllib.request.urlretrieve(url, "abc.html")
url = f"{bash_path}\\abc.html"
f=codecs.open(url, 'r',encoding="utf-8")
text_string = f.read()
soup = BeautifulSoup(text_string, 'html.parser')
all_text = soup.get_text()

l = ["span", "a", "nav", "footer", "header", "footer", "input", "ol", "select", "button", "title", "label", "img"]
for i in l:
    r = soup.findAll(i)
    for p in r:
        p.extract()

g = "".join([s for s in soup.get_text().strip().splitlines(True) if s.strip("\r\n").strip()])
print(g)
with open("sample.txt", "a+", encoding="utf-8") as f:
    f.truncate(0)
    f.write(g)
    f.close()

os.remove(f"{bash_path}\\abc.html")

# to find all links and scrap whole website
# external_links = set()
# internal_links = set()
# for line in soup.find_all('a'):
#     link = line.get('href')
#     if not link:
#         continue
#     if link.startswith(url):
#         external_links.add(link)
#     else:
#         internal_links.add(link)
#
#
# for link in external_links:
#     print(link)
#     urllib.request.urlretrieve(link, "abc.html")
#     url = f"{bash_path}\\abc.html"
#     time.sleep(2)
#     f = codecs.open(url, 'r', encoding="utf-8")
#     text_string = f.read()
#     soup = BeautifulSoup(text_string, 'html.parser')
#     all_text = soup.get_text()
#
#     r = requests.get(link)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     all_text = soup.get_text()
#     l=["span","a","nav","footer","header","footer","input","ol","select","button","title","label","img"]
#     for i in l:
#         r = soup.findAll(i)
#         for p in r:
#             p.extract()
#
#     g = "".join([s for s in soup.get_text().strip().splitlines(True) if s.strip("\r\n").strip()])
#     # print(g)
#     with open("sample.txt", "a+", encoding="utf-8") as f:
#         f.write(link)
#         f.write(g)
#         f.close()
#
#     os.remove(f"{bash_path}\\abc.html")




