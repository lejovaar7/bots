import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from clint.textui import progress
import re
from tkinter.filedialog import askopenfilename
import wget
from tkinter import Tk


ua = UserAgent()

def download_video(videos_hd, name):

    for v in videos_hd:
        print(v)
        r = requests.get(v, stream=True, allow_redirects=True)
        try:
            d = r.headers['content-disposition']
            filename = re.findall("filename=(.+)", d)[0]
        except:
            try:
                wget.download(v, name)
                return
            except Exception as e:
                print(e)
                continue
            continue

        with open(filename, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                if chunk:
                    f.write(chunk)
                    f.flush()
        return

def tubbeoffline_API(url_video):

    s = requests.Session()

    s.headers.update({
        "User-Agent": ua.random
    })


    main_url = "https://www.tubeoffline.com/download-Xhamster-videos.php"

    s.get(main_url)

    url = "https://www.tubeoffline.com/downloadFrom.php"

    querystring = {"host":"Xhamster","video": url_video}

    payload = ""
    headers = {
        'authority': "www.tubeoffline.com",
        'upgrade-insecure-requests': "1",
        'sec-fetch-dest': "document",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'accept-language': "en-US,en;q=0.9"
        }

    response = s.request("GET", url, data=payload, headers=headers, params=querystring)

    html = BeautifulSoup(response.content, "html.parser")

    table = html.find("table")

    trs = table.findAll("tr")
    
    videos_hd = []

    for tr in trs:
        if tr.find("td") == None or tr.find("td").text == "Best":
            continue
        
        if tr.find("td").text == "720p":
            videos_hd.append(tr.find("a")["href"])

    print("*****************+")

    print(videos_hd)
    if len(videos_hd) > 0:
        return videos_hd, s
    else:
        return None, None

root = Tk()
filename = askopenfilename()
root.destroy()

print(filename)

f = open(filename, "r").read().split("\n")

for i in f:
    print(i)

    try:
        videos_hd, session = tubbeoffline_API(i)
        if len(videos_hd) > 0:
            name = i.split("/")[-1] + ".mp4"
            download_video(videos_hd, name)
    except Exception as e:
        print(e)

