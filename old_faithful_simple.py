# -*- coding: utf-8 -*-
"""
Created on Sun Feb 02 19:58:42 2014

@author: Jake
"""

import urllib2 #for API calls to GeyserTimes.org
import json #API returns JSON
import time

"""
  API call for most recent entry for
    Old Faithful (id = 2)
    Daisy (4)    
    Castle (5)
    Riverside (7)
    Grand (13)
    
"""
url = "http://www.geysertimes.org/api/v2/entries_latest/2;4;5;7;13"

content = urllib2.urlopen(url).read()
myJSON = json.loads(content)

#Old Faithful entry is the first in the entries list
old_faithful = myJSON['entries'][0]

window = 10

# if Old Faithful is marked as a minor (i.e. a "short"), use shorter interval 
if old_faithful['min'] == 1:
    interval = 62 #minutes
else:
    interval = 95 #minutes

# slight adjustment for ie times
if old_faithful['ie'] == 1:
    interval = interval - 2
    window = window + 1


myTime = old_faithful['time']

prediction = int(old_faithful['time']) + (interval * 60)
out_prediction = time.strftime('%Y-%m-%d %H:%M', time.gmtime(prediction))



print "Old Faithful is predicted for %s +/- %s minutes" % (out_prediction, window)
print "Send to GeyserTimes.org: {'prediction': %s, 'window': %s}" % (prediction  , window)

