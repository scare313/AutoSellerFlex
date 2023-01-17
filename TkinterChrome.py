
import tkinter as tk
from tkinter import ttk
import webbrowser

import requests
from urllib.request import urlopen

class Browser(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create GUI elements
        self.title("My Browser")
        self.geometry("800x600")

        self.url_entry = ttk.Entry(self)
        self.url_entry.pack(side="top", fill="x")

        self.go_button = ttk.Button(self, text="Go", command=self.go)
        self.go_button.pack(side="top")

        self.web_frame = ttk.Frame(self)
        self.web_frame.pack(side="bottom", fill="both", expand=True)

    def go(self):
        url = self.url_entry.get()

        if not url.startswith("http"):
            url = "http://" + url

        # Open the web page in the default browser
        #webbrowser.open(url)
        response = requests.get(url)
        print(response.text)
        
        print("AAAA"*100)
        response = requests.post(url, data= {'q': 'WHat is this'} )
        print(response.text)

if __name__ == "__main__":
    browser = Browser()
    browser.mainloop()
