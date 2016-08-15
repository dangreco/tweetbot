#  _______                _   _           _   
 #|__   __|              | | | |         | |  
  #  | |_      _____  ___| |_| |__   ___ | |_ 
   # | \ \ /\ / / _ \/ _ \ __| '_ \ / _ \| __|
    #| |\ V  V /  __/  __/ |_| |_) | (_) | |_ 
    #|_| \_/\_/ \___|\___|\__|_.__/ \___/ \__|
    
    # Created by Daniel Greco
    # 8/15/16
    # NOTES:
    # - Ensure that the 0's on lines 34 and 39 are changed to whatever post you want to tweet.
    # - Change hastags on line 39.
    # - You need to create a twitter app + account first.
    # - You need the libraries 'feedparser' and 'twython' for this to work. 
    # - To run this program multiple times, create mulitple copies, changing the entrie number for each one.
    #   By doing so, if one runs and is a duplicate, it will not stop the rest of the tweets from sending. 
    # - This project is OPEN SOURCE; please feel free to submit any changes or improvements to dan.greco@live.com                                       
                                             

#!/usr/bin/env python
import sys
import feedparser
from twython import Twython

# Sets API Tokens and Keys
apiKey = ''
apiSecret = ''
accessToken = ''
accessTokenSecret = ''
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

# Parses RSS Feed Data
feed = feedparser.parse('REPLACE ME WITH RSS URL')
# Grabs title of Entry 0 
title = feed['entries'][0]['title']
# Fixes length to be under 140 Characters if past 70
if len(title) > 70:
    title = title[:70]
# Builds main tweet string    
tweetStr = title + "... #CHANGE #ME " + feed['entries'][0]['link']
# Prevents from Unicode errors
tweetStr = tweetStr.encode('utf-8')
# Sends tweet 
api.update_status(status=tweetStr)
# Prints sent tweet to console
print "Tweeted: " + tweetStr
