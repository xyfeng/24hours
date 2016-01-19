# 24 Hours
A 24-hour poetry composed by 1440 global tweets, part of gallery show 'Clock' at Frog NY 2015

[DEMO](http://xyfeng.github.io/24hours/) ( Data is queried at New York on April 10th, 2015, it happened to be the Apple Watch Pre-Order day )

## How did the data is collected
I used python script to crawl data from twitter search engine in [Iron](http://www.iron.io/) and store it in my [Parse](http://www.parse.com/) account.

## Script
IRON: `iron_worker upload iron`

### Thermal Printer
Download [Gimp-Print](http://gimp-print.sourceforge.net/)

Enable Cups Web Interfaces `cupsctl WebInterface=yes`

Go to URL  `http://127.0.0.1:631/`

Add Printer `Choose 'Raw' as maker`

Check Printer Status `lpstat -p -d`

Print Txt File  `lp -d Thermal_Label_Printer xxxx.txt`

### Linux (Setup using Raspberry Pi)
1. The printer uses a WinBond CDC USB chip, so linux mounts it automatically as /dev/usb/lp0.
2. $ sudo chmod a+rw /dev/usb/lp0
3. $ echo 'Testing 1 2 3' > /dev/usb/lp0
