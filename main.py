import feedparser
import requests
import time

webhook = input("Webhook url: ")

def get_entry(lastEntry):
    NewsFeed = feedparser.parse("https://threatpost.com/feed/")
    entry = NewsFeed.entries[0]

    if lastEntry.title != entry.title:
        res = requests.post(
            webhook,
            headers = {"Content-Type" : "application/json"},
            json = {
                "embeds" : [
                    {
                        "title" : entry.title,
                        "description" : entry.description,
                        "url" : entry.link,
                        "color": 5814783
                    }
                ]
            }
        )
    time.sleep(60)

    get_entry(entry)

get_entry("")
