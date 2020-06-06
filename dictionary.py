from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import messagebox

root= tk.Tk()
root.title("Dictionary")
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

name = tk.Entry (root) 
canvas1.create_window(200, 140, window=name)

def get_definition():
	url = 'https://www.dictionary.com/browse/'
	headers = requests.utils.default_headers()
	global name
	search = name.get()
	headers.update({
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
		})
	print("->",search)
	try:
		req = requests.get(url+search, headers)
		soup = BeautifulSoup(req.content, 'html.parser')

		mydivs = soup.findAll("div", {"value": "1"})[0]

		for tags in mydivs:
			meaning = tags.text
		
		messagebox.showinfo("Definition", meaning)
	except:
		messagebox.showinfo("Definition", "Word not found")


button1 = tk.Button(text='Search Word', command=get_definition)
canvas1.create_window(200, 180, window=button1)

root.mainloop()
