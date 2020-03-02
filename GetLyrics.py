import requests
import json
from bs4 import BeautifulSoup

def getLyrics():
    searchTerm = input("Search term: ")

    params = {"per_page":5, "q":searchTerm}

    r = requests.get("https://genius.com/api/search/multi",params=params)
    songData = json.loads(r.text)["response"]["sections"][0]["hits"][0]["result"]

    assert(songData["_type"] == "song")
    
    rec = input("Is '%s' correct? (y/n) " % songData["full_title"]).lower() 

    if "n" in rec:
        print("Please don't do this > 500 times, python recursion limit will happen\n\n")
        return getLyrics()
    
    lyricsPage = requests.get(songData["url"])

    bs = BeautifulSoup(lyricsPage.text,features="html5lib")

    lyricsTag = bs.find("div",attrs={"class":"song_body-lyrics"})
    
    lyricsText = str(lyricsTag.text)

    while "</html>" in lyricsText:
        lyricsText = lyricsText[lyricsText.find("</html>")+3:]
    
    splitted = lyricsText.split("\n")
    splitted = [i for i in splitted if (len(i)>0 and i[0] != " " and i[0] != "[")]
    
    words = "\n".join(splitted)
    words = words.replace("'","").replace('"','').replace("(","").replace(")","").replace("\n"," ").replace(",","").replace("?","").replace("!","")
    return words.split(" ")
