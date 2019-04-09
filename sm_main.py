from tkinter import *
from time import *
import feedparser

main = Tk()
main.geometry("1500x800+0+0")
main.title("SmartMirror 1.0")
main.resizable(width = False, height = False)
main['bg'] = "black"

import requests

url = "http://api.openweathermap.org/data/2.5/weather?zip=57850,fr&appid=bc7306b4c83ee80239f54b391032d3c6&lang=fr&units=metric"

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
temp = str(temp)

cond = data['weather'][0]['description']
cond = cond.capitalize()

d = feedparser.parse('https://www.francetvinfo.fr/titres.rss')

info = 0
info = int(info)

print("La température est de : {} degrès celcius".format(temp))
print(cond)

heure = strftime("%H {} %M {} %S", localtime()).format(":", ":", ":")
heurel = Label(main, text = heure, font = "Verdana 55 bold")
heurel['bg'] = "black"
heurel['fg'] = "white"
heurel.pack(side = TOP, anchor = W)

ltemp = Label(main, text = temp + "°C", font = "Verdana 50 bold")
ltemp['fg'] = "white"
ltemp['bg'] = "black"
ltemp.pack(side = TOP, anchor = W)

cond = Label(main, text = cond , font = "Verdana 30 bold")
cond['fg'] = "white"
cond['bg'] = "black"
cond.pack(side = TOP, anchor = W)


ville = Label(main, text = "Dabo \n\n", font = "Verdana 25 bold")
ville['fg'] = "white"
ville['bg'] = "black"
ville.pack(side = TOP, anchor = W)

infos = Label(main, text = "Informations :\n", font = "Verdana 15 bold", background = "black")
infos.pack(side = TOP, anchor = W)
infos['fg'] = "white"

headlines = Label(main, font = "Arial 10 bold", background = "black")
headlines.pack(side = TOP, anchor = W)
headlines['fg'] = "white"

for post in d.entries:
	if info < 5:
		print(post.title)
		headlines['text'] += "\n" + post.title
		info += 1
	else:
		pass	


def update_heure():
        heure = strftime("%H {} %M {} %S", localtime()).format(":", ":", ":")
        heurel['text'] = heure
        main.after(500, update_heure)


	






























main.after(500, update_heure) 	
main.mainloop()