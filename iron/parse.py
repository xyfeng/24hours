from TwitterSearch import *
import datetime
import time
import json
import httplib
import urllib

# Get Msg
tso = TwitterSearchOrder()
tso.set_language('en')
tso.set_locale('ja')
tso.set_result_type('recent')
tso.set_count(1)
msg = ''

ts = TwitterSearch(
    consumer_key = 'F8QnORsYQqXiY2zu7FDmxfRsL',
    consumer_secret = '5v7l0GxfUb0ukigxTsvwiGungqWfZjBGv5fSygnXOUGH5JFbph',
    access_token = '17522673-AmQBBeDcHwkwJVtkwxhOW8iESiW5xoVlZeLNMOEIp',
    access_token_secret = 'hRyBq99BDmjXFaCnKTZ3YGVEUaFQz9bP0T7whvV0FFOv7'
)

onehourearlier = datetime.datetime.now() - datetime.timedelta(hours=4)
# onehourearlier = datetime.datetime.now()

currTime = onehourearlier.strftime('%l:%M%p').replace(' ','')
search_word = '#'+currTime
tso.set_keywords([search_word])
try:
    response = ts.search_tweets(tso)
    tweet = response['content']['statuses'][0]
    msg = '@%s: %s' % ( tweet['user']['screen_name'].encode('utf-8'), tweet['text'].encode('utf-8') )

except TwitterSearchException as e:
    print(e)

if currTime.lower() in msg.lower():
    print msg
    # Push to Parse
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    params = urllib.urlencode({"where":json.dumps({
            "timestamp": currTime
         })})
    connection.request('GET', '/1/classes/tweets?%s' % params, '', {
            "X-Parse-Application-Id": "9apBIWvcBtevWLeFPifONqYg8kc1gvojPhBRPytI",
            "X-Parse-REST-API-Key": "ftbwSwgPKg4gq9sVo8twze4fyDpL2McJhThQhA5Z"
         })
    result = json.loads(connection.getresponse().read())
    print result

    if len(result['results']) > 0:
        objectID = result['results'][0]['objectId']
        print objectID
        connection.request('PUT', '/1/classes/tweets/'+objectID, json.dumps({
            "tweet": msg
        }), {
            "X-Parse-Application-Id": "9apBIWvcBtevWLeFPifONqYg8kc1gvojPhBRPytI",
            "X-Parse-REST-API-Key": "ftbwSwgPKg4gq9sVo8twze4fyDpL2McJhThQhA5Z",
            "Content-Type": "application/json"
        })
    else:
        connection.request('POST', '/1/classes/tweets', json.dumps({
            "timestamp": currTime,
            "tweet": msg
        }), {
            "X-Parse-Application-Id": "9apBIWvcBtevWLeFPifONqYg8kc1gvojPhBRPytI",
            "X-Parse-REST-API-Key": "ftbwSwgPKg4gq9sVo8twze4fyDpL2McJhThQhA5Z",
            "Content-Type": "application/json"
        })
    result = json.loads(connection.getresponse().read())
    print result
