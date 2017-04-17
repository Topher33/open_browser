#!/usr/bin/env python

import webbrowser
import schedule
import time

def open_url():
    new = 2 # open in a new tab, if possible
    # open a public URL, in this case, the webbrowser docs
    url_list = ["http://i.imgur.com/MRPlF7l.gifv", "https://utmost.org/"]
    for x in url_list:
        webbrowser.open(x)

schedule.every().day.at("09:30").do(open_url)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
