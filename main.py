import feedparser
import requests
import time

webhook = input("Webhook url: ")

def get_entry(lastEntry):
    NewsFeed = feedparser.parse("https://threatpost.com/feed/")
    entry = NewsFeed.entries[0]

    if lastEntry.title != entry.title:
        requests.post(webhook, data = {"content" : f"```md\n{entry.title}\n{'=' * len(entry.title)}\n{entry.description}\n\n[][ {entry.link} ][]```"})
    time.sleep(60)

    get_entry(entry)

get_entry("")
