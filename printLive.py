import datetime
import time
import json
import httplib
import urllib
import os

oneminuteearlier = datetime.datetime.now() - datetime.timedelta(minutes=1)
printTime = oneminuteearlier.strftime('%l:%M%p').replace(' ','')

while True:
    currTime = time.strftime('%l:%M%p').replace(' ','')
    if currTime != printTime:
        printTime = currTime
        connection = httplib.HTTPSConnection('api.parse.com', 443)
        connection.connect()
        params = urllib.urlencode({"where":json.dumps({
                "timestamp": printTime
             })})
        connection.request('GET', '/1/classes/tweets?%s' % params, '', {
                "X-Parse-Application-Id": "9apBIWvcBtevWLeFPifONqYg8kc1gvojPhBRPytI",
                "X-Parse-REST-API-Key": "ftbwSwgPKg4gq9sVo8twze4fyDpL2McJhThQhA5Z"
             })
        result = json.loads(connection.getresponse().read())['results'][0]

        print result['tweet']

        # Save to File
        text_file = open("toPrint.txt", "w")
        text_file.write("%s\n\n\n" % result['tweet'].encode('utf-8'))
        text_file.close()

        # Print
        os.system("lp -d Thermal_Label_Printer toPrint.txt")
