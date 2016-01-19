import time
import json
import os

data = json.load(open('24h.json'))

printTime = time.strftime('%l:%M%p').replace(' ','')
hourIndex = int(time.strftime('%H'))
while True:
    currTime = time.strftime('%l:%M%p').replace(' ','')
    if currTime != printTime:
        printTime = currTime
        msg = data[hourIndex][printTime]
        text_file = open("toPrint.txt", "w")
        text_file.write("%s\n\n\n" % data[hourIndex][printTime].encode('utf-8'))
        text_file.close()
        os.system("lp -d Thermal_Label_Printer toPrint.txt")
        # print msg
