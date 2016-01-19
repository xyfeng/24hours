from TwitterSearch import *
from datetime import datetime
import time
import json

msgList = []
sleep_for = 5

tso = TwitterSearchOrder()
tso.set_language('en')
tso.set_locale('ja')
tso.set_result_type('recent')
tso.set_count(1)

ts = TwitterSearch(
    consumer_key = 'F8QnORsYQqXiY2zu7FDmxfRsL',
    consumer_secret = '5v7l0GxfUb0ukigxTsvwiGungqWfZjBGv5fSygnXOUGH5JFbph',
    access_token = '17522673-AmQBBeDcHwkwJVtkwxhOW8iESiW5xoVlZeLNMOEIp',
    access_token_secret = 'hRyBq99BDmjXFaCnKTZ3YGVEUaFQz9bP0T7whvV0FFOv7'
)

for h in range(0, 24):
    hourList = {}
    for m in range(0, 60):
        one = datetime(2000, 1, 1, h, m, 0, 0)
        timestamp = one.strftime("%l:%M%p").replace (" ", "")
        print timestamp
        search_word = '#'+timestamp
        tso.set_keywords([search_word])
        try:
            response = ts.search_tweets(tso)
            # print( "rate-limiting status: %s" % ts.get_metadata()['x-rate-limit-remaining'] )

            for tweet in response['content']['statuses']:
                hourList[timestamp] = '@%s: %s' % ( tweet['user']['screen_name'].encode('utf-8'), tweet['text'].encode('utf-8') )
                break

        except TwitterSearchException as e:
            print(e)

        time.sleep(sleep_for)
    msgList.append(hourList)

with open("24h.json", "w") as outfile:
    json.dump(msgList, outfile)
