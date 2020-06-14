import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from tkinter import filedialog, Tk

ua = UserAgent()

root = Tk()

users = filedialog.askopenfilename()


root.destroy()


f = open(users, "r").read().split("\n")
print(f)

for user in f:
    url = f"https://xhamster.com/users/{user}/videos"


    s = requests.Session()


    s.headers.update({
        "User-Agent": ua.random
    })

    while True:
        try:
            r = s.get(url)

            if r.status_code == 404:
                url = f"https://xhamster.com/channels/{user}/"
                r = s.get(url)
                if r.status_code == 404:
                    print("Account not found")
                    break
        except:
            print(f"Error {user}")
            break


        html = BeautifulSoup(r.content, "html.parser")

        videos = html.findAll(class_="video-thumb")

        links = []

        for v in videos:
            if v.find(class_="thumb-image-container__icon--hd") == None:
                continue
            links.append(v.find("a")["href"])
            f = open(f"{user}.txt", "a")
            f.write(v.find("a")["href"] + "\n")
            f.close()

        print(len(links))
        print(links)

        url = html.find("a", {"data-page": "next"})
        
        if url == None:
            break

        url = url["href"]

print("Task finished")