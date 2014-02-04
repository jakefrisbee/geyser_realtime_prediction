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

#dictionary of prediciton parameters
#NPS values as of January 2014
#Castle needs its own method
params = {
  'Old Faithful': {'interval_min': 62, 'interval_max': 95, 'window' : 10, 'ie_interval_adjustment': 2, 'ie_window_adj': 1},
  'Daisy': {'interval_min': 2.75 * 60, 'interval_max': 2.75 * 60, 'window' : 15, 'ie_interval_adjustment': 2, 'ie_window_adj': 1},
  #'Castle': {'interval_min': 62, 'interval_max': 95, 'window' : 10, 'ie_interval_adjustment': 2, 'ie_window_adj': 1},
  'Riverside': {'interval_min': 6 * 60, 'interval_max': 6 * 60, 'window' : 30, 'ie_interval_adjustment': 15, 'ie_window_adj': 10},
  'Grand': {'interval_min': 7.5 * 60, 'interval_max': 7.5 * 60, 'window' : 1.5 * 60, 'ie_interval_adjustment': 5, 'ie_window_adj': 10}
  }


predict('Old Faithful',myJSON['entries'][0])
predict('Daisy',myJSON['entries'][1])
#predict('Castle',myJSON['entries'][2])
predict('Riverside',myJSON['entries'][3])
predict('Grand',myJSON['entries'][4])


def predict(geyser,entry):

  myTime = int(entry['time'])
  
  if entry['min'] == 1 and params[geyser]['interval_min']:
      interval = params[geyser]['interval_min'] #minutes
  else:
      interval = params[geyser]['interval_maj'] #minutes

  window = params[geyser]['window']
  # slight adjustment for ie times
  if entry['ie'] == 1:
      interval = interval - params[geyser]['ie_interval_adjustment']
      window = window + params[geyser]['ie_window_adjustment']

  prediction = int(myTime) + (interval * 60)
  out_prediction = time.strftime('%Y-%m-%d %H:%M', time.gmtime(prediction))

  print "%s Geyser is predicted for %s +/- %s minutes" % (geyser, out_prediction, window)
  print "Send to GeyserTimes.org: {'GeyserID': %s, 'prediction': %s, 'window': %s}" % (entry['geyserID'], prediction  , window)

