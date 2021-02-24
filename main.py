import feedparser
import time

def get_entry(lastEntry):
    NewsFeed = feedparser.parse("https://threatpost.com/feed/")
    entry = NewsFeed.entries[0]

    if lastEntry != entry:
        print(entry.title)
        print(entry.summary)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(60)

    get_entry(entry)

get_entry("")
  
