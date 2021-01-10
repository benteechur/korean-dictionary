import pickle
from bs4 import BeautifulSoup
from datetime import datetime
from os import path
from random import randint
from time import sleep
from urllib.request import urlopen, Request

ids = pickle.load(open("entry_ids.data", "rb"))

base_url = "https://krdict.korean.go.kr/eng/dicSearch/SearchView?nation=eng&ParaWordNo="
pause_beg = 10 #15
pause_end = 19 #30
dir_path = "./pages/"


for entry_id in ids:
    
    fname = dir_path + entry_id + ".html"
    
    if path.exists(fname):
        continue
    
    request = Request(base_url + entry_id, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        response = urlopen(request)   
    except Exception as e:
        print()
        print(f"Entry ID {entry_id} at {datetime.now()}:")
        print(e)
        print()
        
    content = response.read().decode("utf-8")

    f = open(fname, "w", encoding="utf-8")
    f.write(content)
    f.close()
        
    sleep(randint(pause_beg, pause_end))
